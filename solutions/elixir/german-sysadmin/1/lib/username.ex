defmodule Username do
  def sanitize([]), do: []

  def sanitize([head | tail]) do
    case head do
      head when head in 95..122 and head != 96 -> [head] ++ sanitize(tail)
      head when head == 252 -> ~c"ue" ++ sanitize(tail)
      head when head == 246 -> ~c"oe" ++ sanitize(tail)
      head when head == 228 -> ~c"ae" ++ sanitize(tail)
      head when head == 223 -> ~c"ss" ++ sanitize(tail)
      _ -> sanitize(tail)
    end
  end
end
