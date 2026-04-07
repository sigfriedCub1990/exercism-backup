defmodule FreelancerRates do
  def daily_rate(hourly_rate) do
    8.0 * hourly_rate
  end

  def apply_discount(before_discount, discount) do
    discounted_amount = before_discount * (discount / 100)
    before_discount - discounted_amount
  end

  def monthly_rate(hourly_rate, discount) do
    total = 22 * daily_rate(hourly_rate)
    total_discount = total * (discount / 100)
    ceil(total - total_discount)
  end

  def days_in_budget(budget, hourly_rate, discount) do
    calculated_budget = budget / daily_rate(hourly_rate)
    real_budget = Float.ceil(calculated_budget * (discount / 100), 2)
    Float.floor(calculated_budget + real_budget, 1)
  end
end
