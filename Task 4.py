import csv

import xlsxwriter as xlsxwriter

def is_dominated_by_any(beer_style, dominants):
    for dominant in dominants:
        if (beer_style[1] < dominant[1] and beer_style[2] <= dominant[2]) \
                or (beer_style[1] <= dominant[1] and beer_style[2] < dominant[2]):
            return True
    return False


def front(results):

    if len(results) == 1:
        return results

    else:
        t = front(results[0:int(len(results)/2)])
        b = front(results[int(len(results)/2):len(results)])
        m = []  # list containing final results
        for member in b:
            if not is_dominated_by_any(member, t):
                m.append(member)
    return m + t


with open('piwo.csv', newline='', encoding='utf8') as datafile:
    piwo = csv.reader(datafile)

    # The list "results" is going to contain a following set of data for each beer style: average aroma,
    # average appearance, the list of aroma notes and the list of appearance notes.
    results = []
    counter = 0
    for review_beer in piwo:

        if counter == 0:
            counter += 1
            continue

        if len(results) == 0:
            results.append([review_beer[7], float(review_beer[4]), float(review_beer[5]),
                            [float(review_beer[4])], [float(review_beer[5])]])

        else:

            result_saved = False
            for beer_style in results:
                # if the beer style is already in the list of results:
                if beer_style[0] == review_beer[7]:
                    beer_style[1] = (beer_style[1] * len(beer_style[3]) + float(review_beer[4])) \
                                    / (len(beer_style[3]) + 1)
                    beer_style[2] = (beer_style[2] * len(beer_style[4]) + float(review_beer[5])) \
                                    / (len(beer_style[4]) + 1)
                    beer_style[3].append(float(review_beer[4]))
                    beer_style[4].append(float(review_beer[5]))
                    counter += 1
                    result_saved = True
                    break
            # if the beer style is new to the list of results:
            if not result_saved:
                results.append([review_beer[7], float(review_beer[4]), float(review_beer[5]),
                                [float(review_beer[4])], [float(review_beer[5])]])

        counter += 1

    # After the segregation is done, the list "results" is going to be saved into the external xlsx file.
    workbook = xlsxwriter.Workbook("Task_4_results.xlsx")
    worksheet = workbook.add_worksheet("sheet")

    worksheet.write(0, 0, "Beer style")
    worksheet.write(0, 1, "Aroma - average")
    worksheet.write(0, 2, "Appearence - average")
    counter = 1
    for beer_style in results:
        worksheet.write(counter, 0, beer_style[0])
        worksheet.write(counter, 1, beer_style[1])
        worksheet.write(counter, 2, beer_style[2])
        counter += 1

    # After saving the results, it is advisable to pick the best fitting set of beer styles. In order to do this,
    # a recursive function is going to be used in order to find the Pareto set, which basically means finding the
    # set of the best beer styles among the entire set. Before using the "front()" function, it is necessary
    # to sort the results.
    results = sorted(results, key=lambda beer_style: beer_style[1])
    results.reverse()
    pareto_set = front(results)
    worksheet.write(0, 4, "Beer style")
    worksheet.write(0, 5, "Aroma - average")
    worksheet.write(0, 6, "Appearence - average")
    counter = 1
    for beer_style in pareto_set:
        worksheet.write(counter, 4, beer_style[0])
        worksheet.write(counter, 5, beer_style[1])
        worksheet.write(counter, 6, beer_style[2])
        counter += 1



    workbook.close()

