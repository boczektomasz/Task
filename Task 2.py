import csv

with open('piwo.csv', newline='', encoding='utf8') as datafile:
    piwo = csv.reader(datafile)

    # Taking into consideration the fact, that the value inscribed in column "review_overall" is supposed to be
    # presumably most indicative, it will be used as the major determinant of the recommendation. However, it might
    # happen, there will be too many beers, more than 3, with the same note. Therefore, as the second determinant the
    # value of "review_taste" is going to be used, thirdly the "review_aroma" etc. I

    recommended = [[]]
    highest_overall = 0
    forloop_counter = 0
    error_counter = 0

    for review_beer in piwo:

        # The first row is a header:
        if forloop_counter == 0:
            forloop_counter = 1
            continue

        # Since the data file is huge, and there is no possibility to make sure there aren't any mistakes in the cells,
        # which will be used for numerical operations, it is advisable to manage the ValueError.
        try:

            # If the beer has a higher overall note, the "recommended" list will be overwritten.
            if float(review_beer[3]) > highest_overall:
                recommended = [[review_beer[12], review_beer[10], review_beer[3], review_beer[9], review_beer[4],
                                review_beer[8]]]
                highest_overall = float(review_beer[3])

            # if the beer has the same overall note as the beers in the "recommended" list,
            # it will be added to the list.
            elif float(review_beer[3]) == highest_overall:

                already_on_list = False
                # It might though happen, the beer is already in the list:
                for beer in recommended:
                    if review_beer[12] == beer[0]:
                        already_on_list = True
                        break
                if not already_on_list:
                    recommended.append([review_beer[12], review_beer[10], review_beer[3], review_beer[9], review_beer[4],
                                    review_beer[8]])

        except ValueError:
            error_counter += 1

    # Only 3 best beers must be chosen:
    if len(recommended) > 3:
        recommended = sorted(recommended, key=lambda beer: beer[3])
        recommended = sorted(recommended, key=lambda beer: beer[4])
        recommended = sorted(recommended, key=lambda beer: beer[5])
        recommended.reverse()

    count = 0

    print("Beers recommended: ")
    for r in recommended:
        if count < 3:
            print(r[1] + ", ID: " + r[0])
            count += 1
        else:
            break

