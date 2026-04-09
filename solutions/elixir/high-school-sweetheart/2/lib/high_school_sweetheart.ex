defmodule HighSchoolSweetheart do
  def first_letter(name), do: String.trim(name) |> String.first()

  def initial(name), do: first_letter(name) |> String.upcase() |> Kernel.<>(".")

  def initials(full_name) do
    String.split(full_name)
    |> Enum.map(&initial(&1))
    |> Enum.join(" ")
  end

  def pair(full_name1, full_name2) do
    one = initials(full_name1)
    two = initials(full_name2)
    """
    ❤-------------------❤
    |  #{one}  +  #{two} |
    ❤-------------------❤
    """
  end
end
