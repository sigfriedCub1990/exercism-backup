defmodule HighScore do
  defp initial_score(), do: 0

  @high_scores %{}

  def new() do
    @high_scores
  end

  def add_player(scores, name, score \\ 0), do: Map.put(scores, name, score)

  def remove_player(scores, name), do: Map.delete(scores, name)

  def reset_score(scores, name), do: Map.put(scores, name, initial_score())

  def update_score(scores, name, score),
    do: Map.update(scores, name, score, fn previous_score -> previous_score + score end)

  def get_players(scores), do: Map.keys(scores)
end
