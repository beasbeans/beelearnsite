import pickle
import os

def build_dict(filename, dict, dictName): 
    ##makes placeholder dictionary
    dict = {

    }
    ##if there is already a pickle file, we don't have to run the program again, just load the pickle
    if os.path.exists(dictName + ".p"):
        print("Dict " + dictName + " already built")
        dict = pickle.load(open(dictName + ".p", "rb"))
        print("Dict " + dictName + " unpickled")
    else:
        file = open(filename, encoding="UTF-8")
        i = 0
        questans = "init"
        ##while there is text in the line of the file (stops program when finished with file)
        while questans != None and questans != "" :
            questans = file.readline()
             ##cleans the string a bit
            questans = questans.replace("\n", "")
            questans = questans.replace("â¸´", ",")
            questans = questans.replace("ËˆËˆ", '"')
            ##finds the arbitrary breakpoint between q and a
            breakloc = questans.find(" - ttdd")
            ##question is just up to breakpoint
            quest = questans[:breakloc]
            ##answer is jusy whats past breakpoint
            ans = questans[(breakloc + 7):]
            ##appends question and answer to dictionary
            dict[quest] = ans
            i += 1
        ## delete empty final entry
        del dict['']
        print("Dict " + dictName + " built")
        pickle.dump( dict, open( dictName + ".p", "wb" ) )
        print("Dict " + dictName + " pickled")
        print("Dict size: " + str(i))
        file.close()
    return dict

#math = build_dict("math.txt", "math", "math")
#print(list(math)[(len(list(math))-1)])
