# importing Modules
import pandas as pd
import matplotlib.pyplot as plt


# Function to show user the dataframe
def show_data():
    try:
        print("1.Show complete dataframe\n2.Select only a specific column\n3.Show the first amount of rows from a "
              "dataframe\n4.Show the last amount of rows from a dataframe\n5.Show unique values\n6.Show  number of "
              "unique"
              "values\n7.Show column names\n8.Exit")
        opt1 = int(input("..: "))
        if opt1 == 1:
            print(data_df.to_string())
        elif opt1 == 2:
            print("Enter column name")
            col = input("..: ")
            print(data_df[col])
        elif opt1 == 3:
            print("Enter row amount")
            amo = int(input("..: "))
            print(data_df.head(amo))
        elif opt1 == 4:
            print("Enter row amount")
            amot = int(input("..: "))
            print(data_df.tail(amot))

        elif opt1 == 5:
            print("Enter column name")
            colu = input("..: ")
            print(data_df[colu].unique())

        elif opt1 == 6:
            print("Enter column name")
            colu1 = input("..: ")
            print(data_df[colu1].nunique())

        elif opt1 == 7:
            print(data_df.columns)

        elif opt1 == 8:
            main()
        else:
            print("Please Enter a number that's posted above")
    except:
        print("You Entered Some FOOLISHNESS DUMMY")


# Function to show user the dataframe information
def show_data_info():
    try:
        print("1.Show dataframe Info\n2.Show a specific column info\n3.Describe Numeric DataFrame\n4.Exit")

        opt1 = int(input("..: "))
        if opt1 == 1:
            print(data_df.info())
        elif opt1 == 2:
            print("Enter column name")
            col = input("..: ")
            print(data_df[col].info)
        elif opt1 == 3:
            print(data_df.describe())
        elif opt1 == 4:
            main()
        else:
            print("Please Enter a number that's posted above")
    except:
        print("You Entered Some FOOLISHNESS DUMMY")


# Function to show user the dataframe comparison
def data_compy():
    print("Hello Word")


# Function to allow user to modify dataframe
def missing_data():
    try:
        data_df_new = 0
        print("1.Fill By User Input\n2.Fill with previous value\n3.Fill with next value\n4.Fill with previous value by "
              "column\n5.Fill with next value by column\n6.Fill with mean of a column\n7.Fill with min of a "
              "column\n8.Fill with max of a column\n9.Drop Null Rows\n10.Exit")
        opt1 = int(input("..: "))
        if opt1 == 1:
            print("\nEnter Value")
            val = input("..: ")
            data_df_new = data_df.fillna(value=val)
        elif opt1 == 2:
            data_df_new = data_df.fillna(method='pad')
        elif opt1 == 3:
            data_df_new = data_df.fillna(method='bfill')
        elif opt1 == 4:
            data_df_new = data_df.fillna(method='pad', axis=1)
        elif opt1 == 5:
            data_df_new = data_df.fillna(method='bfill', axis=1)
        elif opt1 == 6:
            print("Enter column name")
            col = input("..: ")
            data_df_new = data_df.fillna(value=data_df[col].mean())
        elif opt1 == 7:
            print("Enter column name")
            col = input("..: ")
            data_df_new = data_df.fillna(value=data_df[col].min())
        elif opt1 == 8:
            print("Enter column name")
            col = input("..: ")
            data_df_new = data_df.fillna(value=data_df[col].max())
        elif opt1 == 9:
            data_df_new = data_df.dropna()

        else:
            print("Please Enter a number that's posted above")

        print(data_df_new)
        print("\n1.Save File\n2.Dont Save")
        opt1 = int(input("..: "))
        if opt1 == 1:
            name = str(input("Enter File Name: "))
            data_df_new.to_csv('{}.csv'.format(name), index=False, encoding='utf-8')
        elif opt1 == 2:
            main()
        else:
            print("Please Enter a number that's posted above")
    except:
        print("You Entered Some FOOLISHNESS DUMMY")


# Function to allow user the create aggregate dataframe
def aggregate_function():
    try:
        data_df_new = 0
        print("1.Sum \n2.Min\n3.Average\n4.Max\n5.Count\n6.TOP\n7.\n8.\n9.")
        opt1 = int(input("..: "))

        if opt1 == 1:
            print("\nEnter Column To GroupBy")
            val = input("..: ")
            print("\nEnter Aggregate Column")
            val1 = input("..: ")
            data_df_new = data_df.groupby(val)[[val1]].sum()
        elif opt1 == 2:
            print("\nEnter Column To GroupBy")
            val = input("..: ")
            print("\nEnter Aggregate Column")
            val1 = input("..: ")
            data_df_new = data_df.groupby(val)[[val1]].min()
        elif opt1 == 3:
            print("\nEnter Column To GroupBy")
            val = input("..: ")
            print("\nEnter Aggregate Column")
            val1 = input("..: ")
            data_df_new = data_df.groupby(val)[[val1]].mean()

        elif opt1 == 4:
            print("\nEnter Column To GroupBy")
            val = input("..: ")
            print("\nEnter Aggregate Column")
            val1 = input("..: ")
            data_df_new = data_df.groupby(val)[[val1]].max()

        elif opt1 == 5:
            print("\nEnter Column To GroupBy")
            val = input("..: ")
            print("\nEnter Aggregate Column")
            val1 = input("..: ")
            data_df_new = data_df.groupby(val)[[val1]].value_counts()

        elif opt1 == 6:
            print("\nEnter Column To GroupBy")
            val = input("..: ")
            print("\nEnter Aggregate Column")
            val1 = input("..: ")
            x = data_df.groupby(val)[[val1]].sum()
            data_df_new = x.sort_values(val, ascending=False)

        else:
            print("Please Enter a number that's posted above")

        print(data_df_new)
        print("\n1.Save File\n2.Dont Save")
        opt1 = int(input("..: "))
        if opt1 == 1:
            name = str(input("Enter File Name: "))
            data_df_new.to_csv('{}.csv'.format(name), index=False, encoding='utf-8')
        elif opt1 == 2:
            main()
        else:
            print("Please Enter a number that's posted above")
    except:
        print("You Entered Some FOOLISHNESS DUMMY")


# Function to allow user the create graphs from aggregate dataframe
def plot_graph():
    try:
        plt.style.use('dark_background')
        print("1.Line Graph \n2.BarChart\n3.Horizontal BarChart\n4.PieChart\n5.Exit")
        opt1 = int(input("..: "))

        if opt1 == 1:
            data_df_new = 0
            val = 0
            val1 = 0
            typ = 0
            print("1.Sum \n2.Min\n3.Average\n4.Max\n5.Exit")
            opt1 = int(input("..: "))
            if opt1 == 1:
                typ = "Sum"
                print("\nEnter Column To GroupBy")
                val = input("..: ")
                print("\nEnter Aggregate Column")
                val1 = input("..: ")
                data_df_new = data_df.groupby(val)[[val1]].sum()
            elif opt1 == 2:
                typ = "Minimum"
                print("\nEnter Column To GroupBy")
                val = input("..: ")
                print("\nEnter Aggregate Column")
                val1 = input("..: ")
                data_df_new = data_df.groupby(val)[[val1]].min()
            elif opt1 == 3:
                typ = "Average"
                print("\nEnter Column To GroupBy")
                val = input("..: ")
                print("\nEnter Aggregate Column")
                val1 = input("..: ")
                data_df_new = data_df.groupby(val)[[val1]].mean()
            elif opt1 == 4:
                typ = "Max"
                print("\nEnter Column To GroupBy")
                val = input("..: ")
                print("\nEnter Aggregate Column")
                val1 = input("..: ")
                data_df_new = data_df.groupby(val)[[val1]].max()
            elif opt1 == 5:
                plot_graph()

            plt.plot(data_df_new, color="r", lw=3, linestyle=":")
            plt.xlabel(val)
            plt.ylabel(val1)
            plt.title("Line Graph showing total {} {} of {}".format(typ, val1, val))
            plt.grid()
            plt.show()

        if opt1 == 2:
            data_df_new = 0
            val = 0
            val1 = 0
            typ = 0
            print("1.Sum \n2.Min\n3.Average\n4.Max\n5.Exit")
            opt1 = int(input("..: "))
            if opt1 == 1:
                typ = "Sum"
                print("\nEnter Column To GroupBy")
                val = input("..: ")
                print("\nEnter Aggregate Column")
                val1 = input("..: ")
                data_df_new = data_df.groupby(val)[[val1]].sum()
            elif opt1 == 2:
                typ = "Minimum"
                print("\nEnter Column To GroupBy")
                val = input("..: ")
                print("\nEnter Aggregate Column")
                val1 = input("..: ")
                data_df_new = data_df.groupby(val)[[val1]].min()
            elif opt1 == 3:
                typ = "Average"
                print("\nEnter Column To GroupBy")
                val = input("..: ")
                print("\nEnter Aggregate Column")
                val1 = input("..: ")
                data_df_new = data_df.groupby(val)[[val1]].mean()
            elif opt1 == 4:
                typ = "Max"
                print("\nEnter Column To GroupBy")
                val = input("..: ")
                print("\nEnter Aggregate Column")
                val1 = input("..: ")
                data_df_new = data_df.groupby(val)[[val1]].max()
            elif opt1 == 5:
                plot_graph()

            plt.bar(data_df_new.index, data_df_new[val1])
            plt.xlabel(val)
            plt.ylabel(val1)
            plt.title("BarChart showing total {} {} of {}".format(typ, val1, val))
            plt.grid()
            plt.show()

        if opt1 == 3:
            data_df_new = 0
            val = 0
            val1 = 0
            typ = 0
            print("1.Sum \n2.Min\n3.Average\n4.Max\n5.Exit")
            opt1 = int(input("..: "))
            if opt1 == 1:
                typ = "Sum"
                print("\nEnter Column To GroupBy")
                val = input("..: ")
                print("\nEnter Aggregate Column")
                val1 = input("..: ")
                data_df_new = data_df.groupby(val)[[val1]].sum()
            elif opt1 == 2:
                typ = "Minimum"
                print("\nEnter Column To GroupBy")
                val = input("..: ")
                print("\nEnter Aggregate Column")
                val1 = input("..: ")
                data_df_new = data_df.groupby(val)[[val1]].min()
            elif opt1 == 3:
                typ = "Average"
                print("\nEnter Column To GroupBy")
                val = input("..: ")
                print("\nEnter Aggregate Column")
                val1 = input("..: ")
                data_df_new = data_df.groupby(val)[[val1]].mean()
            elif opt1 == 4:
                typ = "Max"
                print("\nEnter Column To GroupBy")
                val = input("..: ")
                print("\nEnter Aggregate Column")
                val1 = input("..: ")
                data_df_new = data_df.groupby(val)[[val1]].max()
            elif opt1 == 5:
                plot_graph()

            plt.barh(data_df_new.index, data_df_new[val1])
            plt.xlabel(val1)
            plt.ylabel(val)
            plt.title("Horizontal BarChart showing total {} {} of {}".format(typ, val1, val))
            plt.grid()
            plt.show()

        if opt1 == 4:
            data_df_new = 0
            val = 0
            val1 = 0
            typ = 0
            print("1.Sum \n2.Min\n3.Average\n4.Max\5.Exit")
            opt1 = int(input("..: "))
            if opt1 == 1:
                typ = "Sum"
                print("\nEnter Column To GroupBy")
                val = input("..: ")
                print("\nEnter Aggregate Column")
                val1 = input("..: ")
                data_df_new = data_df.groupby(val)[[val1]].sum()
            elif opt1 == 2:
                typ = "Minimum"
                print("\nEnter Column To GroupBy")
                val = input("..: ")
                print("\nEnter Aggregate Column")
                val1 = input("..: ")
                data_df_new = data_df.groupby(val)[[val1]].min()
            elif opt1 == 3:
                typ = "Average"
                print("\nEnter Column To GroupBy")
                val = input("..: ")
                print("\nEnter Aggregate Column")
                val1 = input("..: ")
                data_df_new = data_df.groupby(val)[[val1]].mean()
            elif opt1 == 4:
                typ = "Max"
                print("\nEnter Column To GroupBy")
                val = input("..: ")
                print("\nEnter Aggregate Column")
                val1 = input("..: ")
                data_df_new = data_df.groupby(val)[[val1]].max()
            elif opt1 == 5:
                plot_graph()

            plt.pie(data_df_new[val1], labels=data_df_new.index, autopct="%.2f%%", pctdistance=0.9,
                    startangle=90)
            plt.legend(bbox_to_anchor=(0.02, 1.1), title="{}".format(val))
            plt.title("Horizontal PieChart showing total {} {} of {}".format(typ, val1, val))
            plt.grid()
            plt.show()
        elif opt1 == 5:
            main()
        else:
            print("Please Enter a number that's posted above")
    except:
        print("You Entered Some FOOLISHNESS DUMMY")


# Function to predict the further
def time_forcast():
    print("hello world")


# main menu
def main():
    try:
        print(
            "1.Show Data\n2.Show Data information\n3.Data Compy\n4.Handling missing data\n5.Aggregate functions\n6.Plot"
            "Graphs\n7.Time Forecasting\n8.Exit")
        opt = int(input("..: "))
        if opt == 1:
            show_data()
        elif opt == 2:
            show_data_info()
        elif opt == 3:
            data_compy()
        elif opt == 4:
            missing_data()
        elif opt == 5:
            aggregate_function()
        elif opt == 6:
            plot_graph()
        elif opt == 7:
            time_forcast()
        elif opt == 8:
            pass
        else:
            print("Please Enter a number that's posted above")
    except:
        main()


while True:
    try:
        # Finds File and converts it into a dataframe
        print("Enter Your file name")
        d = input("..: ")
        data = pd.read_csv('{}.csv'.format(d))
        data_df = pd.DataFrame(data)
        main()
    except:
        print("Invalid Filename")
