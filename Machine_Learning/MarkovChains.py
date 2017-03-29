import markovify
import pandas as pd

file = pd.read_csv('comments.csv',sep='|')
df = pd.DataFrame(file)

del df['sub_title']
del df['img_link']
del df['sub_id']
del df['blankk']

model_list = []
score_weights = []
excepted = 0
for i in range(0,len(df['comment_body'])):
    try:
        if type(df['comment_body'][i]) != 'str':
            text_model = markovify.Text(df['comment_body'][i], state_size=3)
            model_list.append(text_model)
            score_weights.append(df['comment_score'][i]) 
        else:
            excepted += 1
    except(TypeError):
        print('Comment Excepted at index: ' + str(i))
#print(excepted)

print(len(score_weights))

model_combo = markovify.combine(model_list,score_weights)
model_combo.make_short_sentence(100)

