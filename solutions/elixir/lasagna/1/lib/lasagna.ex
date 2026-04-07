defmodule Lasagna do
  def expected_minutes_in_oven, do: 40

  def remaining_minutes_in_oven(elapsed_min) do
    expected_minutes_in_oven() - elapsed_min
  end

  def preparation_time_in_minutes(layers_count), do: 2 * layers_count

  def total_time_in_minutes(layers_count, elapsed_min) do
    preparation_time_in_minutes(layers_count) + elapsed_min
  end

  def alarm, do: "Ding!"
end
