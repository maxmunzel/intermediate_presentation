import marimo

__generated_with = "0.6.0"
app = marimo.App()


@app.cell
def __():
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    return np, pd, plt


@app.cell
def __(pd):
    df = pd.read_csv(
        "/Users/casparfriedrich/Downloads/wandb_export_2024-06-13T11_21_36.289+02_00.csv",
        index_col="simulation_steps",
    )
    return df,


@app.cell
def __(df):
    df.head()
    return


@app.cell
def __(df):
    for key in df:
        if "MIN" in key or "MAX" in key or "_step" in key:
            del df[key]
    for key in df:
        data = df[key]
        del df[key]
        new_key = key.split("-")[0].strip()
        df[new_key] = data
    return data, key, new_key


@app.cell
def __(df):
    df.head(50)
    return


@app.cell
def __(df, np, plt):
    fig, ax = plt.subplots(figsize=(6, 5))
    for i, k in enumerate(df):
        if "mocap" in k:
            continue
        df[k].dropna().plot(ax=ax, linewidth=3)
    ax.legend(loc="upper right")
    ax.set_xticks(1e7 * np.arange(6), [f"{i}M" for i in range(0, 60, 10)])
    ax.set_xlabel("Simulation Steps")
    ax.set_ylabel("Evaluation Success Rate (Sim)")
    ax.set_ylim(0, 1)
    ax.grid(True, axis="y")
    fig.savefig("media/clipping_reward.pdf")
    fig

    fig, ax = plt.subplots(figsize=(6, 5))
    for i, k in enumerate(df):
        if not "clipped" in k or "mocap" in k:
            continue
        df[k].dropna().plot(ax=ax, linewidth=3, label=k.replace("clipped", "")+" Episode")
    ax.legend(loc="upper right")
    ax.set_xticks(1e7 * np.arange(6), [f"{i}M" for i in range(0, 60, 10)])
    ax.set_xlabel("Simulation Steps")
    ax.set_ylabel("Evaluation Success Rate (Sim)")
    ax.set_ylim(0, 1)
    ax.grid(True, axis="y")
    fig.savefig("media/training.pdf")
    fig
    return ax, fig, i, k


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
