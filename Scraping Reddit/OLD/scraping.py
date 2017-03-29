sub = reddit.subreddit('RoastMe')
comments = open('comments.csv','w')
for submission in sub.top(limit=20):
    try:
        print(str(submission))
        submission.comment_sort = 'top'
        print("Post ID: " + submission.id)
        submission.comments.replace_more(limit=0)
        submission.comments.replace_more(threshold=0)
        for top_level_comment in submission.comments.list():
                comment = top_level_comment.body
                comment = str.join(' ', comment.splitlines())
                csvline = submission.id + ',"' + submission.title + '",' + submission.url + ',"' + str(top_level_comment.score) + ',' + comment + '"\n'
                comments.write(csvline)
            except UnicodeEncodeError:
                pass
    except:
        print('Error on submission_id: ' + str(submission))