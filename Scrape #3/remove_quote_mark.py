with open("/Users/jason/Desktop/Hortaçsu/Electricity-Project/Scrape #3/ngasdata_missing.csv", "r") as data:
    with open("/Users/jason/Desktop/Hortaçsu/Electricity-Project/Scrape #3/ngasdata_missing_fixed.csv", "w") as output:
        for line in data:
            quote_counter = 0
            quote_list = []
            comma_counter = 0
            i = 0
            for char in line:
                if char == "\"":
                    quote_counter += 1
                    quote_list.append(i)
                if char == ",":
                    comma_counter += 1
                if comma_counter == 1:
                    break
                i += 1
            if quote_counter > 2:
                j = 1
                newline = line
                while j < len(quote_list) - 1:
                    newline = newline[0:quote_list[j]] + "!" + newline[(quote_list[j] + 1):len(newline)]
                    j += 1
                output.write(newline)
            else:
                output.write(line)