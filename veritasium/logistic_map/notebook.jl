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

# ╔═╡ e338d842-7719-11eb-35c6-efdf74875751
using PlutoUI

# ╔═╡ e80655b8-76c5-11eb-1438-85fd5054780b
next_logistic(x, growth_rate=2.6) = growth_rate .* x .* (1 .- x) 

# ╔═╡ 54a5bd48-76c6-11eb-18fa-65a57e2be14f
begin
  x = 0:.001:1
  y = next_logistic.(x);
end

# ╔═╡ cf72f62e-76c6-11eb-3389-d343b8217f7b
plot(x, y, dpi=200, legend=false)

# ╔═╡ ddb1a95a-7730-11eb-0c51-19fc37d551eb
md"""
#### Negative feedback loop
In the sense, once an iteration get a high $x_n$, the next iteration $x_{n+1}$ will be mapped to a small value.

"""

# ╔═╡ 41ab4ace-76c8-11eb-1779-eb7d95ed3842
#@bind n Slider(1:100, default=1, show_value=true)

# ╔═╡ d3ae7692-7724-11eb-30d6-091451792d46
md"""
`n` $(@bind n Slider(1:1000, default=1, show_value=true))
$(html"<br>")
`x1` $(@bind x1 Slider(0:0.01:1, default=.4, show_value=true))
$(html"<br>")
`r` $(@bind r Slider(0:0.1:999_999_999, default=2.6, show_value=true))
"""

# ╔═╡ bfd9a498-76c7-11eb-07c7-ad7d1144d4d7
begin
  xn = x1
  for i in 1:n
    xn = next_logistic(xn, r)
  end
  xn
end

# ╔═╡ aebdfe54-7731-11eb-3ad4-e1a139ada52f
begin
  length = 50
  xs = [0. for _ in 1:length]
  xs[1] = x1
  for i in 2:length
	xs[i] = next_logistic(xs[i-1], r)
  end
  xs
end	

# ╔═╡ 0e9528c8-7734-11eb-0e4a-bf65284ad4aa
md"""
**tweak** the intial population `x1` to observe that the convergent value changes
- not with `x1`
- but with `r`
"""

# ╔═╡ 79ddeee2-7733-11eb-2f04-0132bae963ff
begin
  good_dpi = 300
  plot(xs, dpi=good_dpi)
  scatter!(xs, dpi=good_dpi, ylims=(0,1),
		title="r = $r,  x1 = $(x1)\nxs[$(length)] = $(xs[end])", legend=false)
end

# ╔═╡ Cell order:
# ╠═e80655b8-76c5-11eb-1438-85fd5054780b
# ╠═b1a8e446-76c6-11eb-2474-874d4bc0a9cc
# ╠═54a5bd48-76c6-11eb-18fa-65a57e2be14f
# ╠═cf72f62e-76c6-11eb-3389-d343b8217f7b
# ╟─ddb1a95a-7730-11eb-0c51-19fc37d551eb
# ╠═e338d842-7719-11eb-35c6-efdf74875751
# ╠═41ab4ace-76c8-11eb-1779-eb7d95ed3842
# ╟─d3ae7692-7724-11eb-30d6-091451792d46
# ╠═bfd9a498-76c7-11eb-07c7-ad7d1144d4d7
# ╠═aebdfe54-7731-11eb-3ad4-e1a139ada52f
# ╟─0e9528c8-7734-11eb-0e4a-bf65284ad4aa
# ╟─79ddeee2-7733-11eb-2f04-0132bae963ff
