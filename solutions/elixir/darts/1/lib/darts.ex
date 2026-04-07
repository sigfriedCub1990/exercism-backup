defmodule Darts do
  @type position :: {number, number}

  @doc """
  Calculate the score of a single dart hitting a target
  """
  @spec score(position) :: integer
  def score({x, y}) do
    result = :math.sqrt((x ** 2) + (y ** 2))
    cond do
      result > 10 -> 0
      result > 5 and result <= 10 -> 1
      result > 1 and result <= 5 -> 5
      result <= 1 -> 10
      true -> 0
    end
  end
end
