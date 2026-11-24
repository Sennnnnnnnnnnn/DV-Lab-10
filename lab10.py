
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------------
# 1. Page configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Lab 10 | Framing the Data Story",
    layout="wide"
)

st.title("Framing the Data Story")
st.caption("Data Visualization | Lab 10")

# --------------------------------------------------
# 2. Audience and purpose
# --------------------------------------------------
st.sidebar.header("Audience Settings")

audience = st.sidebar.selectbox(
    "Select your audience",
    [
        "Students",
        "Workshop Instructor",
        "Department Manager"
    ]
)

if audience == "Students":
    purpose = "Understand which data visualization skills need improvement."
    takeaway = "Data storytelling is the main area where students need support."
    chart_title = "Students Need More Support in Data Storytelling"

elif audience == "Workshop Instructor":
    purpose = "Decide which topic should receive the most attention during the workshop."
    takeaway = "Prioritize data storytelling when planning the next workshop."
    chart_title = "Prioritize Data Storytelling in the Next Workshop"

else:
    purpose = "Identify skill areas that may require additional training support."
    takeaway = "Data storytelling has the lowest average rating and may need targeted training."
    chart_title = "Data Storytelling Is the Main Training Priority"

st.subheader("Audience and Purpose")

st.write(f"**Audience:** {audience}")
st.write(f"**Purpose:** {purpose}")
st.info(f"**Key takeaway:** {takeaway}")

# --------------------------------------------------
# 3. Sample data and rating adjustment
# --------------------------------------------------
st.header("Student Skill Ratings")

st.caption(
    "Fictional example averages, not findings from a real survey."
)

skills = [
    "Data storytelling",
    "Python",
    "Chart selection",
    "Color and labels",
    "Data cleaning"
]

default_ratings = [2.4, 3.0, 3.2, 3.7, 4.1]

st.sidebar.header("Adjust Ratings")

ratings = []

for skill, default in zip(skills, default_ratings):
    rating = st.sidebar.slider(
        skill,
        min_value=1.0,
        max_value=5.0,
        value=default,
        step=0.1
    )
    ratings.append(rating)

df = pd.DataFrame({
    "Skill": skills,
    "Average rating": ratings
})

# Identify the lowest-rated skill dynamically
lowest_index = df["Average rating"].idxmin()
lowest_skill = df.loc[lowest_index, "Skill"]
lowest_rating = df.loc[lowest_index, "Average rating"]

# --------------------------------------------------
# 4. Dynamic takeaway
# --------------------------------------------------
st.subheader("Updated Key Finding")

st.success(
    f"{lowest_skill} has the lowest average rating "
    f"at {lowest_rating:.1f} out of 5."
)

# --------------------------------------------------
# 5. Audience-focused chart
# --------------------------------------------------
st.header("Skill Rating Comparison")

fig, ax = plt.subplots(figsize=(9, 5))

bar_colors = [
    "#E07A3F" if i == lowest_index else "#4C78A8"
    for i in range(len(skills))
]

bars = ax.barh(
    df["Skill"],
    df["Average rating"],
    color=bar_colors
)

ax.set_xlim(0, 5)
ax.set_xticks(range(0, 6))

ax.set_xlabel(
    "Average self-rating (1 = beginner, 5 = confident)"
)

ax.set_title(
    f"{lowest_skill} Received the Lowest Average Rating"
)

ax.invert_yaxis()
ax.grid(axis="x", color="#DDDDDD", linewidth=0.7)
ax.set_axisbelow(True)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Display rating labels
for bar, value in zip(bars, ratings):
    ax.text(
        value + 0.05,
        bar.get_y() + bar.get_height() / 2,
        f"{value:.1f}",
        va="center"
    )

# Add one annotation to emphasize the lowest rating
ax.annotate(
    "Main area for improvement",
    xy=(
        lowest_rating,
        bars[lowest_index].get_y()
        + bars[lowest_index].get_height() / 2
    ),
    xytext=(3.0, lowest_index - 0.6),
    arrowprops=dict(arrowstyle="->"),
    fontsize=9
)

fig.tight_layout()
st.pyplot(fig, clear_figure=True)

st.caption(
    "Fictional practice values. Ratings represent average self-ratings "
    "on a scale from 1 to 5. The orange bar highlights the lowest rating."
)

# --------------------------------------------------
# 6. Explain the graphic
# --------------------------------------------------
st.header("Understanding the Chart")

with st.expander("How to interpret this graphic"):
    st.write(
        "**Category axis:** Lists five data visualization skills."
    )

    st.write(
        "**Numeric axis:** Shows average self-ratings from 1 to 5."
    )

    st.write(
        "**Bar lengths:** Represent the average rating for each skill."
    )

    st.write(
        "**Orange bar:** Highlights the skill with the lowest rating."
    )

    st.write(
        "**Level of detail:** Each value is an average, not an "
        "individual student's response."
    )

    st.write(
        f"**Key takeaway:** {lowest_skill} is the area that "
        "should receive the most attention."
    )

# --------------------------------------------------
# 7. Compare the original and revised story
# --------------------------------------------------
st.header("Lesson 3: Reframe the Story")

st.write("**Original audience:** Students")
st.write(
    "**Original takeaway:** Data storytelling received the "
    "lowest average rating (2.4 out of 5)."
)

st.write(f"**New audience:** {audience}")
st.write(f"**Revised takeaway:** {takeaway}")

st.caption(
    "Changing the audience changes the explanation and the decision "
    "being supported, even when the underlying data remains the same."
)

# --------------------------------------------------
# 8. Audience feedback
# --------------------------------------------------
st.header("Evaluate the Story")

st.write(
    "Show the chart to a classmate without reading the takeaway aloud. "
    "Record their feedback below."
)

understood = st.text_area(
    "One point your classmate understood"
)

unclear = st.text_area(
    "One point that was unclear"
)

revision = st.text_area(
    "What change did you make after receiving feedback?"
)

if st.button("Save Feedback Notes"):
    if understood and unclear and revision:
        st.success("Feedback notes recorded in this session.")
        st.write("**Understood:**", understood)
        st.write("**Unclear:**", unclear)
        st.write("**Revision:**", revision)
    else:
        st.warning("Please complete all three feedback fields.")

# --------------------------------------------------
# 9. Assignment reflection
# --------------------------------------------------
st.header("Reflection")

st.write(
    "Visual emphasis helps the audience notice the most important "
    "information without having to compare every value equally. "
    "In this chart, the orange bar highlights the skill with the "
    "lowest average rating, while the other bars use a consistent "
    "color. This makes the main finding easier to identify. "
    "The title also explains the key message instead of using "
    "a general heading. Explanatory text helps the audience "
    "understand what the axes, bar lengths, and average ratings "
    "represent. It also clarifies that the values are fictional "
    "practice averages rather than actual survey findings. "
    "However, visual emphasis must be used carefully because "
    "highlighting a value without enough context could mislead "
    "the audience. The chart should therefore include clear "
    "labels, an appropriate scale, and a short explanation. "
    "Feedback from classmates can also reveal whether viewers "
    "understand the intended message. Overall, combining visual "
    "emphasis with explanatory text helps the audience understand "
    "the finding and remember the main takeaway."
)

