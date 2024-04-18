library(httr)
library(remotes)
library(dplyr)
library(ggplot2)
library(tidyr)
library(jsonlite)

get_paginated <- function(query, max_gets = 250) {
  out <- vector("list", max_gets)
  get_next <- TRUE
  first <- TRUE
  gets <- 0
  pb <- txtProgressBar(0, max_gets, 1, style = 3)
  while (get_next & gets < max_gets) {
    tryCatch(
      {
        if (first) {
          raw_response <- httr::GET(
            url = endpoint_url,
            query = query
          )
        }
        else {
          raw_response <- httr::GET(query)
        }
        first <- FALSE
        response <- httr::content(raw_response, as = "parsed")
        
        gets <- gets + 1
        out[[gets]] <- response
        get_next <- is.null(response[["paging"]][["next"]]) #false if there is a next page
        get_next <- !get_next
        if (get_next & gets < max_gets) {
          query <- response[["paging"]][["next"]]
          setTxtProgressBar(pb, gets)
        }
        Sys.sleep(10)
      },
      error = function(e) {
        warning("Most recent call produced an error. Returning last available results.")
        warning(e)
        get_next <<- FALSE
      }
    )
  }
  setTxtProgressBar(pb, max_gets)
  close(pb)
  if (gets == 0) {
    stop("No results returned")
  }
  return(out)
}

get_from_url <- function(query, max_gets = 100) {
  out <- vector("list", max_gets)
  get_next <- TRUE
  gets <- 0
  pb <- txtProgressBar(0, max_gets, 1, style = 3)
  while (get_next & gets < max_gets) {
    tryCatch(
      {
        raw_response <- httr::GET(query)
        first <- FALSE
        response <- httr::content(raw_response, as = "parsed")
        
        gets <- gets + 1
        out[[gets]] <- response
        get_next <- is.null(response[["paging"]][["next"]]) #false if there is a next page
        get_next <- !get_next
        if (get_next & gets < max_gets) {
          query <- response[["paging"]][["next"]]
          setTxtProgressBar(pb, gets)
        }
        Sys.sleep(8)
      },
      error = function(e) {
        warning("Most recent call produced an error. Returning last available results.")
        warning(e)
        get_next <<- FALSE
      }
    )
  }
  setTxtProgressBar(pb, max_gets)
  close(pb)
  if (gets == 0) {
    stop("No results returned")
  }
  return(out)
}

# *****************************************

getwd()
setwd("/Users/jasminezhang/thesis/collected_ads")

endpoint_url <- "https://graph.facebook.com/v18.0/ads_archive"

keywords <- c("replace with your keywords")

#query from keyword
for (i in seq_along(keywords)) {
  currentKeyword <- keywords[i]
  print(paste("Keyword: ", currentKeyword))
  
  my_query <- list(
    search_terms = currentKeyword,
    search_type = "KEYWORD_EXACT_PHRASE",
    ad_reached_countries = "US",
    languages = 'en',
    limit = "250",
    fields = "ad_creative_bodies, id, ad_creation_time, ad_snapshot_url, ad_creative_link_captions, ad_creative_link_descriptions, ad_creative_link_titles, ad_delivery_start_time, ad_delivery_stop_time, languages, page_id, page_name, bylines, delivery_by_region, demographic_distribution, estimated_audience_size, impressions, spend",
    access_token = "your_token"
  )
  
  ads <- get_paginated(my_query)
  
  json_file_name <- paste0(currentKeyword, "_output.json")
  
  print(json_file_name)
  
  json_data <- toJSON(ads)
  writeLines(json_data, json_file_name)
}

# *****************************

#query from URL
for (i in seq_along(keywords)) {
  currentKeyword <- keywords[i]
  print(paste("Keyword: ", currentKeyword))
  
  my_query <- list(
    search_terms = currentKeyword,
    search_type = "KEYWORD_EXACT_PHRASE",
    ad_reached_countries = "US",
    languages = 'en',
    limit = "250",
    fields = "ad_creative_bodies, id, ad_creation_time, ad_snapshot_url, ad_creative_link_captions, ad_creative_link_descriptions, ad_creative_link_titles, ad_delivery_start_time, ad_delivery_stop_time, languages, page_id, page_name, bylines, delivery_by_region, demographic_distribution, estimated_audience_size, impressions, spend",
    access_token = "your_token"
    )
  
  ads_ctd <- get_from_url("https://graph.facebook.com/v18.0/ads_archive?search_terms=drug&search_type=KEYWORD_EXACT_PHRASE&ad_reached_countries=US&languages=en&limit=100&fields=ad_creative_bodies%2C%20id%2C%20ad_creation_time%2C%20ad_snapshot_url%2C%20ad_creative_link_captions%2C%20ad_creative_link_descriptions%2C%20ad_creative_link_titles%2C%20ad_delivery_start_time%2C%20ad_delivery_stop_time%2C%20languages%2C%20page_id%2C%20page_name%2C%20bylines%2C%20delivery_by_region%2C%20demographic_distribution%2C%20estimated_audience_size%2C%20impressions%2C%20spend&access_token=EAAKOqxRyBVwBOZCzPObHYc97lgRXMR23ao8ETPSRxtoSI3AmnGkuOMZBEXy3ToeZAiHZBrqZC7LiseWJUYR0FNNM8ML9E3ITOrnv6pXkkUI7t7zuwT0ZC2xoipYEGPJJuCKfJGkPaOmUtbmxBOAgFGIr8xHwma3r9pUApO5XmxbrIXzdBBN4kcFgMsb5xqC5YKG5vtnUIl&after=c2NyYXBpbmdfY3Vyc29yOk1UWTBOVGd3T1RFNE1qbzJPVFUyTlRjMU9ERTBPRE16T1RVPQZDZD")
  
  json_file_name <- paste0(currentKeyword, "2_output.json")
  
  print(json_file_name)
  
  json_data <- toJSON(ads_ctd)
  writeLines(json_data, json_file_name)
}
