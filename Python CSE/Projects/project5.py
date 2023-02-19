''' Insert heading comments here.'''


def open_file():
    '''Insert docstring here.'''
    while True:
        filename = input(strings.FILE_PROMPT)
    try:
        fp = open(filename, "r", encoding="utf-8")
        return fp
    except FileNotFoundError:
        print(strings.FILE_ERROR.format(filename))
    
def find_max(num, name, max_num, max_name):
    '''Insert docstring here.'''
    if num < max_num:
        return max_num, max_name
    else:
        if max_name:
            max_name += "\n\t{}".format(name)
        else:
            max_name = "{}\n\t{}".format(max_name, name)
        return num, max_name
    pass  # insert your code here
    
    
def find_min(num, name, min_num, min_name):
    '''Insert docstring here.'''
    if num > min_num:
        return min_num, min_name 
    else:
        if num < min_num:
            name = "\n\t{}".format(name)
            return num, name
        else: 
            min_name ="{}\n\t{}".format(min_name, name)
            return min_num, min_name 

def read_file(data_fp):
    # initialize variables for max and min scores/episodes
    max_score = 0.0
    max_score_name = ""
    max_episodes = 0.0
    max_episode_name = ""
    min_score = float('inf')
    min_score_name = ""
    total_score = 0.0
    score_count = 0

    # read the file line by line
    for line in data_fp:
        # extract title, score, and episodes from the line
        title = line[0:100].strip()
        score_str = line[100:105].strip()
        episodes_str = line[105:110].strip()

        # ignore lines with N/A scores or episodes
        if score_str == "N/A" or episodes_str == "N/A":
            continue

        # convert score and episodes to floats
        score = float(score_str)
        episodes = float(episodes_str)

        # update max and min scores/episodes if necessary
        if score > max_score:
            max_score = score
            max_score_name = title
        if episodes > max_episodes:
            max_episodes = episodes
            max_episode_name = title
        if score < min_score:
            min_score = score
            min_score_name = title

        # update total score and count for computing the average
        total_score += score
        score_count += 1

    # compute average score
    if score_count > 0:
        avg_score = round(total_score / score_count, 2)
    else:
        avg_score = 0.0

    return max_score, max_score_name, max_episodes, max_episode_name, min_score, min_score_name, avg_score



    
        
def search_anime(data_fp, anime_name): 
    '''Insert docstring here.'''
    pass  # insert your code here


def main():
    
    BANNER = "\nAnime-Planet.com Records" \
             "\nAnime data gathered in 2022"
    
    MENU ="Options" + \
          "\n\t1) Get max/min stats" + \
          "\n\t2) Search for an anime" + \
          "\n\t3) Stop the program!" + \
          "\n\tEnter option: "
    
    print(BANNER)
    option = ''
    while option != '3':
        option = input(MENU)
        if option == '3':
            print("\nThank you using this program!")
            break
        elif option == '2':
            input("\nEnter filename: ")
            continue
        elif option == '1':
            name = input("\nEnter filename: ")
            print("\n\nAnime with the highest score of {}:".format(find_max(name)))
            continue
        else:
            print("\nInvalid menu option!!! Please try again!")
            continue

# These two lines allow this program to be imported into other code
# such as our function tests code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.
#DO NOT CHANGE THESE 2 lines  
if __name__ == "__main__":
    main()