import keybert

doc = """
         The Covid vaccines made by Pfizer-BioNTech and Moderna may be linked to a slight increase in the risk of stroke when administered along with a high-dose flu vaccine, according to a new analysis by the Food and Drug Administration.

The high-dose flu vaccine is usually given to older people, and the risk association is clearest in adults aged 85 and older. But that increase, if real, seems very small, and it is possible that the risk may stem from the flu vaccine alone.

A separate analysis by the agency points to a small increase in the incidence of seizures after Covid vaccinations in children ages 2 to 5. The papers were posted online last week, and have not yet been vetted for publication in a scientific journal. Experts in vaccine safety said the studies were well done.

Neither study is definitive, and even if these links were confirmed, the increases are so slight that the benefits of vaccination still far outweigh the risks, especially in older adults, experts said. Flu and Covid themselves both raise the risk of stroke.

Although the findings do not warrant a change to vaccine recommendations, they are suggestive enough to merit further study, the experts said.

“Without these types of efforts, the absence of data, the absence of evidence, just leads to a lot of misperceptions,” said Dr. Susan Cheng, a cardiologist and epidemiologist at the Smidt Heart Institute at Cedars Sinai in Los Angeles.

The F.D.A. did not make the researchers available for interviews. In a statement, Cherie Duvall-Jones, a spokeswoman for the agency, said it was “making this information known at this time through publication of this paper for transparency.”

Both studies are based on observational data, which cannot identify cause and effect. The agency is planning to study the occurrence of seizures in children after vaccination “using a more robust design,” Ms. Duvall-Jones said.

“Sometimes, similar small associations of increased risk are not confirmed upon further investigation,” she added.

Administration of flu and Covid vaccines at the same time — or with a single shot that combines both, once one becomes available — is an increasingly popular strategy with health officials aiming to increase vaccine uptake and ease logistical burdens, said Marco Cavaleri, who heads the office of biological health threats and vaccines strategy at the European Medicines Agency.

“That’s the way for the future,” Dr. Cavaleri said. “We, of course, need to be sure that indeed this is a good strategy also from a safety perspective.”

Dr. Cavaleri said he was not yet convinced that the increase in stroke risk was real. Strokes and related health problems occur frequently among those aged 85 or older, he noted. “We have to be extremely careful in not overinterpreting data before we get really large data sets, maybe from different regions, that could tell us exactly what is going on,” he said.

Officials in the United States first noted a possible association about a year ago. At the time, data from the Vaccine Safety Datalink, a federal safety surveillance system, suggested that Americans aged 65 or older might be at increased risk of an ischemic stroke, which interrupts blood supply to the brain, within 21 days of receiving the Pfizer-BioNTech bivalent vaccine offered last fall.

But federal officials said in January that a deeper investigation suggested that a link was “very unlikely,” and that other surveillance systems, including those in other countries, had not found a connection.

In the new study, researchers at the F.D.A. and the Centers for Medicare and Medicaid Services analyzed stroke risk among nearly 5.4 million Medicare beneficiaries aged 65 years or older. They looked at the health records of those who received a Covid bivalent shot either on its own or along with the flu vaccine between Aug. 31 and Nov. 6, 2022.

Their initial analysis found no statistically significant increases in stroke with the Covid vaccines administered by themselves. When federal researchers broke down the data by age, they found an increased risk of stroke among those who were 85 years or older who got the Pfizer-BioNTech vaccine, and in those who were 65 to 74 who got the Moderna vaccine.

The link was most consistent when the bivalent Covid shot was given at the same time as a high-dose flu vaccine or one containing an adjuvant, a chemical added to elicit a stronger immune response.

Those who received both Covid and flu vaccines saw a 20 percent increase in the risk of ischemic stroke with the Pfizer-BioNTech bivalent shot, and an increase of 35 percent in the risk of transient ischemic stroke after the Moderna bivalent shot. (The bivalent shots were replaced in September with new formulations.)

The researchers then looked more closely at the relationship between the flu vaccine and stroke in nearly 7 million Medicare participants who received a high-dose or adjuvanted flu vaccine. They found a small but statistically significant increase, of about 9 percent, in the risk of stroke after receiving the flu vaccine alone.

The results suggest that the high-dose flu vaccine itself may be responsible for the increase in strokes observed in the study, Daniel Salmon, director of the Institute for Vaccine Safety at Johns Hopkins Bloomberg School of Public Health, said.

The study found some odd patterns, however — for example, an increased risk of some types of stroke with the flu vaccine in those ages 65 to 74 and those 85 or older, but not among those who were 75 to 84.

“That’s the sort of thing that would make me wonder if there might be something weird going on in their data, because you would expect there to be more consistency,” Dr. Salmon said.

Federal researchers also calculated a separate measure called attributable risk, or the increase in risk that can be attributed to the exposure. Except in those 85 or older, the attributable risk was roughly three additional cases of stroke for every 100,000 people vaccinated with the Covid vaccine.

The numbers are too small to warrant alarm, Dr. Salmon said, especially because the diseases themselves also carry a risk of stroke.

“If I tell you that your risk of getting struck by lightning doubled, I wouldn’t really sweat it, to be honest with you, because your risk of getting hit by lightning is pretty small,” he said. “Because the background rate is so small, a doubling of that risk isn’t very much.”

Experts also said they were not surprised or concerned by the findings regarding seizures among vaccinated children.

In that study, F.D.A. researchers looked at the incidence of 21 health outcomes in more than 4.1 million children after immunization with the original Covid-19 vaccines made by Pfizer-BioNTech, Moderna and Novavax.

The researchers based their analysis on commercial claims in insurance databases, as well as vaccination data from local and state systems.

The analysis confirmed a previously observed risk of uncommon heart problems after the Pfizer-BioNTech Covid shots in children aged 12 to 17.

The study also detected a small rise in the incidence of seizures and convulsions after the Moderna or Pfizer-BioNTech shots, but only among children aged 2 to 5.

A consistent trend in seizures across all age groups would have been more worrisome. But young children are prone to seizures when they have a high fever, Dr. Cheng said, and other vaccines that produce fevers are known to induce seizures in very young children.

“We know that the Covid vaccines can cause a fever, so it’s not a terribly surprising finding if it’s true,” Dr. Salmon said of the seizures.

Children are at much smaller risk of Covid than older adults, so many parents have opted not to vaccinate them. The low numbers make it challenging to study potential risks, experts noted.

“I commend them for doing the work,” Dr. Salmon said of the F.D.A.’s research. “I do wish they were done earlier, but it’s great that the studies are being done.”

      """
kw_model = keybert.KeyBERT()
kw_model.extract_keywords(doc, keyphrase_ngram_range=(1, 2), stop_words=None)
keywords = kw_model.extract_keywords(doc)
print(keywords)