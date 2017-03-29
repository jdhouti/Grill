import pandas as pd
import ast

file = pd.read_csv('a_new_hope_testFile.csv', sep="|")
file2 = open('forChris.csv', 'w')
df = pd.DataFrame(file)
string = "img_id|tags\n"
file2.write(string)

# convert the line
for i in range(0,len(df['image_description'])):
    try:
        dict7 = ast.literal_eval(df['image_description'][i])
        # collect tags
        try:
            tags = dict7['description']['tags']
            tag_string = ''
            for tag in tags:
                tag_string += tag + ' '
        except IndexError as e:
            tags = ''

        try:
            # collect gender
            gender = dict7['faces'][0]['gender']

            # collect age
            age = dict7['faces'][0]['age']
        except IndexError as e:
            gender = ''
            age = ''
        # collect id
        id = df['image_id'][i]

        final_string = id + "|" + str(age) + " " + gender + " " + tag_string

        file2.write(final_string + "\n")
    except Exception as e:
        print(e)
        print(i)
        file2.write(df['image_id'][i] + "|\n")