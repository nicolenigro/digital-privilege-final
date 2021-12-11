import json
import os

def sort_subreddits(savepath, filename):
    with open(filename) as jsonfile:
        lines = jsonfile.readlines()

        for line in lines:
            reader = json.loads(line)
            subreddit = reader['subreddit']
            # fullpath = savepath + subreddit + '/'
            full_file = os.path.join(savepath, subreddit + '/' + subreddit + ".txt")


            text_packet = ""
            if os.path.isfile(full_file):

                text_packet = ""
                for post in reader['posts']:
                    if not 'body' in post.keys():
                        continue

                    text_packet += post['body']  

                with open(full_file, 'a', encoding="utf-8") as fo:
                    fo.write("\n" + text_packet)
                    fo.close()
                    continue
            
            else:

                if os.path.isdir(savepath + subreddit):
                    text_packet = ""
                    for post in reader['posts']:
                        if not 'body' in post.keys():
                            continue

                        text_packet += post['body']  

                    with open(full_file, 'w', encoding='utf-8') as fo:
                        fo.write("\n" + text_packet)
            
                else:
                    os.makedirs(savepath + subreddit)

                    text_packet = ""
                    for post in reader['posts']:
                        if not 'body' in post.keys():
                            continue

                        text_packet += post['body'] 

                    with open(full_file, 'w', encoding="utf-8") as fo:
                        fo.write(text_packet)
                        fo.write("\n")

           
            print("processed: " + subreddit)

def main():

    savepath = 'subreddits/'
    filename = 'coarse_discourse_dump_reddit.json'
    
    sort_subreddits(savepath, filename)

if __name__ == "__main__":
    main()
