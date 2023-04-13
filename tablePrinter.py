#tablePrinter.py takes a list of lists of strings and siplays it in a well organized talbe with each column right justified

def printTable(table):
    colWidths =[0] * len(table)

    lengthOfLists = len(table[0])


    for tableLen in range(len(table)):
        sortedTable = sorted(table[tableLen], key = len)
        colWidths[tableLen] = len(sortedTable[-1])


    for stringIndex in range(lengthOfLists):
        print()

        for listIndex in range(len(table)):

            string = table[listIndex][stringIndex]

            print(string.rjust(colWidths[listIndex]), end = ' ')



tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]


printTable(tableData)
