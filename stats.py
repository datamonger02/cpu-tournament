import pandas as pd


def load_data():
    df = pd.read_csv(r"CPU_tournament_data_1-11.csv")
    df["Fight ID"] = range(1, len(df) + 1)
    # Create separate DataFrames for each player
    p1 = df[["Fight ID", "Player 1", "Player 1 Slot", "Character 1", "Character 1 Alt", "Winner", "Tournament No.",
             "Round No."]].rename(
        columns={
            "Player 1": "Player",
            "Player 1 Slot": "Player Slot",
            "Character 1": "Character",
            "Character 1 Alt": "Character Alt"
        })

    p2 = df[["Fight ID", "Player 2", "Player 2 Slot", "Character 2", "Character 2 Alt", "Winner", "Tournament No.",
             "Round No."]].rename(
        columns={
            "Player 2": "Player",
            "Player 2 Slot": "Player Slot",
            "Character 2": "Character",
            "Character 2 Alt": "Character Alt"
        })

    # Concatenate the DataFrames
    final_df = pd.concat([p1, p2], ignore_index=True)

    # Drop unnecessary columns
    final_df.drop(columns=["Winner"], inplace=True)

    # Create a new column "Winner" with boolean values
    final_df["Winner"] = final_df.apply(lambda row: row["Player"] == df.loc[row["Fight ID"] - 1, "Winner"], axis=1)

    final_df = final_df.sort_values(by="Fight ID").reset_index(drop=True)

    final_df.rename(columns={"Tournament No.": "Tournament", "Round No.": "Round"})

    return final_df


def character_stats(character, alt):
    # load data
    df = load_data()

    # Number of Wins and losses

    # Highest Round

    # Match History


if __name__ == "__main__":
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    character_stats(load_data())

