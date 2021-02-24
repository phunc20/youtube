### A Pluto.jl notebook ###
# v0.12.20

using Markdown
using InteractiveUtils

# This Pluto notebook uses @bind for interactivity. When running this notebook outside of Pluto, the following 'mock version' of @bind gives bound variables a default value (instead of an error).
macro bind(def, element)
    quote
        local el = $(esc(element))
        global $(esc(def)) = Core.applicable(Base.get, el) ? Base.get(el) : missing
        el
    end
end

# ╔═╡ b1a8e446-76c6-11eb-2474-874d4bc0a9cc
using Plots

# ╔═╡ f81ced94-76c8-11eb-0e4a-918a418b267d
#using InteractiveUtils, PlutoUI
using PlutoUI

# ╔═╡ e80655b8-76c5-11eb-1438-85fd5054780b
next_logistic(x, r=2.6) = r .* x * (1-x) 

# ╔═╡ 54a5bd48-76c6-11eb-18fa-65a57e2be14f
begin
  x = 0:.001:1
  y = next_logistic.(x);
end

# ╔═╡ cf72f62e-76c6-11eb-3389-d343b8217f7b
plot(x, y, dpi=200)

# ╔═╡ 67b1c086-76c8-11eb-0051-c3dfee2a0722
macro bind(def, element)
  quote
    local el = $(esc(element))
    global $(esc(def)) = Core.applicable(Base.get, el) ? Base.get(el) : missing
    el
  end
end


# ╔═╡ 41ab4ace-76c8-11eb-1779-eb7d95ed3842
#@bind n Slider(1:100, default=1, show_value=true)
@bind n Slider(1:100, show_value=true)

# ╔═╡ e8e090d8-76c8-11eb-02f4-cfc1b36f2637
n

# ╔═╡ bfd9a498-76c7-11eb-07c7-ad7d1144d4d7
begin
  x0 = .4
  xn = x0
  for i in 1:n
    xn = next_logistic(xn)
  end
  xn
end

# ╔═╡ Cell order:
# ╠═e80655b8-76c5-11eb-1438-85fd5054780b
# ╠═b1a8e446-76c6-11eb-2474-874d4bc0a9cc
# ╠═54a5bd48-76c6-11eb-18fa-65a57e2be14f
# ╠═cf72f62e-76c6-11eb-3389-d343b8217f7b
# ╠═f81ced94-76c8-11eb-0e4a-918a418b267d
# ╠═41ab4ace-76c8-11eb-1779-eb7d95ed3842
# ╠═e8e090d8-76c8-11eb-02f4-cfc1b36f2637
# ╠═bfd9a498-76c7-11eb-07c7-ad7d1144d4d7
# ╟─67b1c086-76c8-11eb-0051-c3dfee2a0722
