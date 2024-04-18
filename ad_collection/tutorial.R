install.packages("devtools")

devtools::install_github("facebookresearch/Radlibrary", force = TRUE)
library(Radlibrary)

# User-friendly setup that asks you for app ID and secret.
adlib_setup()

# This exchanges the short term token for the long term one.
adlib_set_longterm_token()

# You can verify that the token has been set correctly.
token_get()

search_vector <- c("diabetes", "vaccine", "cancer")
table_vector <- c("diabetes_table", "vaccine_table", "cancer_table")
fb_ad_list <- vector(mode = "list", length = length(search_vector))
names(fb_ad_list) <- table_vector

for (i in seq_along(search_vector)) {
  print(paste("Keyword: ", search_vector[i]))
  
  query <- adlib_build_query(
    ad_reached_countries = "US",
    search_terms = search_vector[i],
    ad_active_status = "ACTIVE",
    publisher_platform = "FACEBOOK",
    fields = c("ad_creative_bodies", "id")
  )
  
  # The call is limited to 1000 results but pagination of overcomes it.
  # We pipe the output of the paginated call to the as_tibble function.
  fb_ad_list[[table_vector[i]]] <- adlib_get_paginated(query,
  token = "your_token"
  )%>%
    as_tibble(
      type = table_type_vector[i],
      censor_access_token = TRUE
    )
}


