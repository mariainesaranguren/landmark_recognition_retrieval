''' Analyzes results from csv files created from newtest2.py '''

import sys

def get_average(l):
    return (sum(l)/len(l))

print (len(sys.argv))
if len(sys.argv) != 2 or sys.argv[1] == "-h":
    print ("Usage: python analyze_predictions.py results.csv")
    exit()
input_file = sys.argv[1]

# Parses csv files
f = open(input_file, "r")
results = f.readlines()
landmark_confidence = {}                # landmark_id : [confidence]
landmark_rank = {}                      # landmark_id : [rank]
all_confidence = []
all_rank = []
f.close()

for img in results:
    img = img[:-2]
    img_result = img.split(",")
    landmark_id = img_result[0]
    img_id = img_result[1].split(".")[0]
    rank = float(img_result[2])
    confidence = float(img_result[3])

    all_rank.append(rank)
    all_confidence.append(confidence)

    if landmark_id in landmark_confidence.keys() and landmark_id in landmark_rank.keys():
        landmark_confidence[landmark_id].append(confidence)
        landmark_rank[landmark_id].append(rank)
    else:
        landmark_confidence[landmark_id] = [confidence]
        landmark_rank[landmark_id] = [rank]

# Total number of predictions
print ("Total number of predictions made:\t", len(all_rank))

# Weighted score
# Confidence is 0 if it is not in one of the top five guesses
weighted_score = sum(all_confidence)
print ("Summation of all confidences:\t\t", weighted_score)
print ("^ Perfect identification with complete confidence would give", len(all_rank))

# Count of each rank
count_rank = {}
for rank in all_rank:
    if rank in count_rank.keys():
        count_rank[rank] += 1
    else:
        count_rank[rank] = 1
print ("Count of each rank level:\t\t", count_rank)

# Average confidence and rank per landmark:
average_landmark_confidence = []        # List of average confidence of each landmark
average_landmark_rank = []              # List of average rank of each landmark
for landmark_id in landmark_confidence.keys():
    average_landmark_confidence.append(get_average(landmark_confidence[landmark_id]))
    average_landmark_rank.append(get_average(landmark_rank[landmark_id]))

print ("Overall average landmark confidence:\t", get_average(average_landmark_confidence))
print ("Overall average landmark rank:\t\t", get_average(average_landmark_rank))













#