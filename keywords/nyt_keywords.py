import spacy
import pytextrank
import csv

input_path = '/Users/jasminezhang/thesis/nytarticles.csv'
output_path = '/Users/jasminezhang/thesis/extractednyt.csv'

# example text
# text = "Pharmacies Shared Patient Records Without a Warrant, an Inquiry Finds. A congressional investigation found that the nation’s largest pharmacies have handed over prescription records to law enforcement without a warrant, raising privacy concerns. Law enforcement agencies have obtained the prescription records of thousands of Americans from the country’s largest pharmacy chains without a warrant, a congressional inquiry found, raising concerns about how the companies handle patient privacy. Three of the largest pharmacy groups — CVS Health, Kroger and Rite Aid — do not require their staff members to contact a lawyer before releasing information requested by law enforcement, the inquiry found. The other five — Walgreens, Cigna, Optum Rx, Walmart and Amazon — said that they do require a legal review before honoring such requests. The policies were revealed on Tuesday in a letter to Xavier Becerra, the secretary of health and human services, from Senator Ron Wyden of Oregon and Representatives Pramila Jayapal of Washington and Sara Jacobs of California, all Democrats. The inquiry began in June, a year after the Supreme Court ended the constitutional right to an abortion and cleared the way for Republican-controlled states to enact near-total bans on the procedure. Reproductive health advocates and some lawmakers have since raised privacy concerns regarding access to birth control and abortion medication. “Although pharmacies are legally permitted to tell their customers about government demands for their data, most don’t,” the lawmakers wrote. “As a result, many Americans’ prescription records have few meaningful privacy protections, and those protections vary widely depending on which pharmacy they use.” More on Abortion Issues in America. Abortion Pill Case: The Supreme Court announced that it would decide on the availability of a commonly used abortion pill — the first major case involving abortion on its docket since it overturned the constitutional right to the procedure. Texas Case: The Texas Supreme Court overturned a lower court order that allowed an abortion for a woman whose fetus was diagnosed with a fatal condition, hours after she decided to leave the state for the procedure. On the Ballot: After voters in Ohio approved a measure to enshrine abortion rights in the State Constitution, could Florida be next? Crossing the Border: American women are traveling to Mexico for abortions, crystallizing the shifting policies of two nations that once held vastly different positions on the procedure. The inquiry found that the pharmacies receive tens of thousands of legal requests annually for their patients’ pharmacy records. However, the letter said, the companies indicated that a vast majority of the requests were submitted in connection with civil litigation. In July, nearly 50 Democratic members of Congress wrote to Mr. Becerra to urge the Health and Human Services Department to expand regulations under the Health Insurance Portability and Accountability Act, or HIPAA, that would require law enforcement agencies to obtain a warrant to gain access to medical records and would require that patients be notified when their records are requested. Since then, lawmakers have been digging into the disclosure practices of major pharmacy chains. During the congressional inquiry, CVS, Kroger and Rite Aid “indicated that their pharmacy staff face extreme pressure to immediately respond to law enforcement demands and, as such, the companies instruct their staff to process those requests in the store,” Mr. Wyden, Ms. Jayapal and Ms. Jacobs wrote in their letter to Mr. Becerra. “Americans’ prescription records are among the most private information the government can obtain about a person,” the lawmakers wrote. “They can reveal extremely personal and sensitive details about a person’s life.” “Pharmacies can and should insist on a warrant, and invite law enforcement agencies that insist on demanding patient medical records with solely a subpoena to go to court to enforce that demand,” the letter said. In a statement, a CVS spokeswoman said that the company’s “processes are consistent with HIPAA” and that its pharmacy teams are trained to “appropriately respond to lawful requests.” “We have suggested a warrant or judge-issued subpoena requirement be considered and we look forward to working cooperatively with Congress to strengthen patient privacy protections,” the spokeswoman, Amy Thibault, said. The Health and Human Services Department has already taken steps to add language to HIPAA that would protect data involving reproductive health. In April, the department’s Office for Civil Rights proposed a rule that would bar health care providers and insurers from turning over information to state officials who are trying to prosecute someone for seeking or providing a legal abortion. Michelle Mello, a professor of law and health policy at Stanford, said that requiring a warrant instead of a subpoena for the release of pharmacy records would “not necessarily preclude concerns” about privacy. She also said that notifying patients about record disclosures, which the lawmakers said “would be a major step forward for patient transparency,” would likely occur only after the fact. While Professor Mello said most pharmacy records should be kept private, she said that targeting pharmacy employees, who could be found in contempt of court for not complying with a law enforcement demand for records, adds another layer of complexity. “It’s not fair to put the onus on them to be found in contempt of court and then fight that,” she said. But efforts by congressional Democrats to shore up HIPAA reveal a longstanding misconception about the health care privacy law, which was signed into law in 1996, she said. “People think HIPAA has broader protection than it does,” Professor Mello said. “It wasn’t designed to enable health care providers to resist very misguided, in my view, attempts to enforce laws that impact patients in a negative way.”"


# load a spaCy model, depending on language, scale, etc.
nlp = spacy.load("en_core_web_sm")

# add PyTextRank to the spaCy pipeline
nlp.add_pipe("topicrank")

# # examine the top-ranked phrases in the document
# for phrase in doc._.phrases:
#     print(phrase.text)
#     print(phrase.rank, phrase.count)
#     print("*******")
#     # print(phrase.chunks)

with open(input_path, 'r') as input, open(output_path, 'w', newline='') as output:
    reader = csv.reader(input)
    writer = csv.writer(output)
    # for phrase in doc._.phrases[:10]:
    #     file.write(phrase.text + '\n')
    for row in reader: 
        doc = nlp(row[0].lower())

        for phrase in doc._.phrases[:5]:
            # output.write(phrase.text + ": ")
            print(phrase.chunks)
            print(type(phrase.chunks))
            # chunks = phrase.chunks.split()
            output_chunks = [phrase.text] + phrase.chunks
            writer.writerow(output_chunks)
            # for chunk in phrase.chunks:
            #     output.write(str(chunk) + " ")
            #output.write('\n')