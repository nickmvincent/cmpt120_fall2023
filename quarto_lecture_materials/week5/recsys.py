# select a user + init variables to keep track of scores
index_of_user = 17
top_score = 0
top_record = ""
recommendation = ""

# load data
with open("./fake_data.csv", "r") as file:
    all_lines = file.readlines()
    header = all_lines[0]
    records = all_lines[1:]

    user_record = records[index_of_user].strip().split(",")

    # use a loop to go through all other record lines (one record = one user)
    for record in records:
        columns = record.strip().split(",")

        if user_record[0] == columns[0]:
            print("Skipping ", record)
            continue

        score_for_current_record = 0
        # split each record line into a list of items
        
        # use a nested loop to go through each item
        # use manually defined [1,3,4] to get only
        # favorite_movie, party, diet
        for column_index in [1,3,4]:
            if columns[column_index] == user_record[column_index]:
                score_for_current_record += 1
        
        if score_for_current_record > top_score:
            top_score = score_for_current_record
            top_record = record
            recommendation = columns[2]

print("You are", user_record)

print("After careful consideration, we have found that the most similar user is")
print(top_record)
print(f"You have a similarity score of {top_score}")

print("We recommend you watch", recommendation)