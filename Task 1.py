import csv

with open('piwo.csv', newline='', encoding='utf8') as datafile:
    piwo = csv.reader(datafile)

    strongest_brewery = [[]]
    highest_abv = 0

    forloop_counter = 0
    error_counter = 0
    for data_row in piwo:

        # The first row is a header:
        if forloop_counter == 0:
            forloop_counter = 1
            continue

        # Since the data file is huge, and there is no possibility to make sure there aren't any mistakes in the cells,
        # which will be used for numerical operations, it is advisable to manage the ValueError.
        try:

            # If the considered beer has higher abv than the highest found so far, it will overwrite the data in
            # the "strongest" list.
            if float(data_row[11]) > highest_abv:
                strongest_brewery = [[data_row[0], data_row[1], data_row[11]]]
                highest_abv = float(data_row[11])

            # If the considered beer has the same abv as the highest found so far, it will add another brewery to
            # the "strongest" list.
            elif float(data_row[11]) == highest_abv:

                already_on_list = False
                # It might though happen, the brewery is already in the list:
                for brewery in strongest_brewery:
                    if data_row[0] == brewery[0]:
                        already_on_list = True
                        break

                # After checking, whether the particular brewery has been inscribed to the list yet, the brewery can be
                # saved in the list.
                if not already_on_list:
                    strongest_brewery.append([data_row[0], data_row[1], data_row[11]])

        except ValueError:
            error_counter += 1

    if len(strongest_brewery) > 1:
        print("The strongest beers are produced accordingly in: ")
        for brewery in strongest_brewery:
            print("Brewery " + brewery[1] + ", highest abv " + brewery[2])
    else:
        print("The strongest beer is produced in " +
              strongest_brewery[0][1] + ", the brewery ID: " +
              strongest_brewery[0][0] + ". The strongest beer produced there reaches ABV of " +
              strongest_brewery[0][2] + "%.")




        
