import argparse
import pandas as pd
import spacy
from utils_app import check, plot_ym
import matplotlib.pyplot as plt
from pandas.core.frame import DataFrame


def plot_ym(df: DataFrame, year_month_start: str, year_month_finish: str) -> None:
    """Takes Dataframe and time interval in string formats and plot bar plot for task_1"""
    df_sliced = df[df["pubdate_y_m"] >= year_month_start][
        df[df["pubdate_y_m"] >= year_month_start]["pubdate_y_m"] <= year_month_finish
    ]
    x = df_sliced.groupby(["pubdate_y_m"])["pubdate_y_m"].count().keys()

    plt.figure(figsize=(20, 10))
    plt.barh(x, df_sliced.groupby(["pubdate_y_m"])["pubdate_y_m"].count().tolist())
    plt.xlabel("Количество документов", size=15)
    plt.ylabel("год-месяц", size=15)
    plt.title("Агрегация количества документов по месяцу-году", size=17)
    plt.savefig("1task_bar_plot.png")


def main():

    parser = argparse.ArgumentParser(description="Data aggregation.")
    parser.add_argument("task_name", choices=["1_task", "2_task", "3_task"])
    parser.add_argument("-s", "--start", help="start - start date string")
    parser.add_argument("-e", "--end", help="end - end date string")

    args = parser.parse_args()
    df = pd.read_csv("data_for_agg/data.csv")

    df["pubdate_y_m"] = df["pubdate"].map(lambda x: "-".join(x.split("-")[:2]))

    if args.task_name == "1_task":
        if args.start == None or args.end == None:
            print("Need to specify start and end dates")
        else:
            year_month_start, year_month_finish = args.start, args.end
            plot_ym(df, year_month_start, year_month_finish)
    elif args.task_name == "2_task":
        if args.start == None or args.end == None:
            print("Need to specify start and end dates")
        else:
            year_month_start, year_month_finish = args.start, args.end
            df_sliced = df[df["pubdate_y_m"] >= year_month_start][
                df[df["pubdate_y_m"] >= year_month_start]["pubdate_y_m"]
                <= year_month_finish
            ]
            agg_df_ymc = (
                df_sliced.groupby(["pubdate_y_m", "categories"])["pubdate_y_m"]
                .count()
                .to_frame()
            )
            agg_df_ymc.rename(
                columns={"pubdate_y_m": "pubdate_y_m_count"}, inplace=True
            )
            agg_df_ymc.to_csv("2_task.csv")
    elif args.task_name == "3_task":

        def check(word):
            if word.pos_ == "ADP" or word.pos_ == "PRON":
                return False
            else:
                return True

        def cleaning(text):
            try:
                doc = nlp(text)
                return " ".join([str(x) for x in doc if check(x)])
            except:
                # пустой article body
                pass

        nlp = spacy.load("en_core_web_sm")
        df["article_body_cleaned"] = df["article_body"].map(cleaning)
        df.to_csv("3_task.csv")


if __name__ == "__main__":
    main()
