defmodule FreelancerRates do
  def daily_rate(hourly_rate) do
    8.0 * hourly_rate
  end

  def apply_discount(before_discount, discount) do
    real_discount = before_discount * (discount / 100)
    before_discount - real_discount
  end

  def monthly_rate(hourly_rate, discount) do
    monthly_rate = 22 * daily_rate(hourly_rate)
    ceil(apply_discount(monthly_rate, discount))
  end

  def days_in_budget(budget, hourly_rate, discount) do
    discounted_daily_rate = apply_discount(daily_rate(hourly_rate), discount)
    Float.floor(budget / discounted_daily_rate, 1)
  end
end
