defmodule HighScore do
  @high_scores %{}

  def new() do
    @high_scores
  end

  def add_player(scores, name, score \\ nil)

  def add_player(scores, name, nil), do: Map.put(scores, name, 0)
  def add_player(scores, name, score), do: Map.put(scores, name, score)

  def remove_player(scores, name), do: Map.delete(scores, name)

  def reset_score(scores, name), do: Map.put(scores, name, 0)

  def update_score(scores, name, score),
    do: Map.update(scores, name, score, fn previous_score -> previous_score + score end)

  def get_players(scores), do: Map.keys(scores)
end
