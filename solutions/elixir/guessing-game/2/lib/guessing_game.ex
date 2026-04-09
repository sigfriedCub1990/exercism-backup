defmodule GuessingGame do
  def compare(_secret_number, guess \\ nil)

  def compare(_secret_number, nil) do
    "Make a guess"
  end
  def compare(_secret_number, :no_guess) do
    "Make a guess"
  end
  def compare(secret_number, guess) do
    difference = guess - secret_number
    cond do
      difference == 0 -> "Correct"
      difference == 1 or difference == -1 -> "So close"
      difference > 1 -> "Too high"
      difference < 0 -> "Too low"
      true -> "Shouldn't reach this"
    end
  end
end
