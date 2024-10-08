

# COLORS FOR DF
def status_color(val):
    if val == "Offer":
        return "background-color: green;"
    elif val == "Rejected":
        return "background-color: red;"
    elif val == "Interviewing":
        return "background-color: coral;"
    elif val == "Applied":
        return "background-color: blue;"
    else:
        return ""
    
    # DATAFRAME STYLES
def style_df(df):
    styled_df = (
        df.style.map(lambda x: "background-color: gray;", subset=["Company"])
        .map(lambda x: "background-color: darkcyan;", subset=["Position"])
        .map(status_color, subset=["Status"])
        # .map(lambda x: 'background-color: purple;', subset=['Website URL'])
        .map(lambda x: "background-color: darkorange;", subset=["Applied Date"])
    )
    return styled_df

