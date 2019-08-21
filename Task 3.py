import csv


# For this task, the idea is basically doing an investigation of the average deviations of particular indicators
# from the overall review note. The bigger the deviation is, the less significant the indicator is.
with open('piwo.csv', newline='', encoding='utf8') as datafile:
    piwo = csv.reader(datafile)

    # In the following variables the average deviation from the overall note is going to be saved:
    aroma_dev = 0
    taste_dev = 0
    appearance_dev = 0
    palette_dev = 0

    counter = 0
    for review_beer in piwo:

        if counter == 0:
            counter += 1
            continue
        elif counter == 1:
            aroma_dev = abs(float(review_beer[3]) - float(review_beer[4]))
            taste_dev = abs(float(review_beer[3]) - float(review_beer[9]))
            appearance_dev = abs(float(review_beer[3]) - float(review_beer[5]))
            palette_dev = abs(float(review_beer[3]) - float(review_beer[8]))
            counter += 1
            continue

        aroma_dev = (aroma_dev * (counter - 1) + abs(float(review_beer[3]) - float(review_beer[4]))) / counter
        taste_dev = (taste_dev * (counter - 1) + abs(float(review_beer[3]) - float(review_beer[9]))) / counter
        appearance_dev = (appearance_dev * (counter - 1) + abs(float(review_beer[3]) - float(review_beer[5]))) / counter
        palette_dev = (palette_dev * (counter - 1) + abs(float(review_beer[3]) - float(review_beer[8]))) / counter

        counter += 1

    print(aroma_dev, taste_dev, appearance_dev, palette_dev)



