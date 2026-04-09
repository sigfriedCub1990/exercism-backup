defmodule GuessingGame do
  def compare(_secret_number, guess \\ nil)

  def compare(_secret_number, nil),
    do: "Make a guess"
  def compare(_secret_number, :no_guess),
    do: "Make a guess"
  def compare(secret_number, guess) when guess - secret_number  == 0,
    do: "Correct"
  def compare(secret_number, guess)
      when guess - secret_number  == -1
      when guess - secret_number  == 1 do
    "So close"
  end
  def compare(secret_number, guess) when guess - secret_number > 1,
    do: "Too high"
  def compare(secret_number, guess) when guess - secret_number < 0,
    do: "Too low"
end
