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
    # load and filter data
    df = load_data()
    df = df[(df["Character"] == character) & (df["Character Alt"] == alt)]

    print("Character Stats for " + character + ", Alt Number " + str(alt))

    # Number of Wins and losses
    win_count = df["Winner"].value_counts().get(True, 0)
    loss_count = df["Winner"].value_counts().get(False, 0)
    win_percent = win_count / (win_count + loss_count) * 100
    print("Number of Wins: " + str(win_count))
    print("Number of Losses: " + str(loss_count))
    print("Win rate: " + str(win_percent) + "%")

    # Highest Round
    won_tournament_rows = df[(df["Round No."] == 5) & (df["Winner"] == True)]
    if not won_tournament_rows.empty:
        # If True, print "Won Tournament Number" with the Tournament No. value
        tournament_no = won_tournament_rows.iloc[0]["Tournament No."]
        print(f"Won Tournament Number: {tournament_no}")
    else:
        # If False, print "Highest Round" with the maximum in the "Round No." column
        highest_round = df["Round No."].max()
        temp = "Error"
        if highest_round == 1:
            temp = "First Round"
        elif highest_round == 2:
            temp = "Sweet 16"
        elif highest_round == 3:
            temp = "Quarterfinals"
        elif highest_round == 4:
            temp = "Semifinals"
        print("Highest Round: " + temp)

    # Match History


if __name__ == "__main__":
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    character_stats("Sonic", 5)

