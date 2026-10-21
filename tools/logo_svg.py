# Builds the animated header logo (inline SVG). The rocket flies under the globe and up the
# right side; a glowing "fire" streak follows it while the trail draws in, then fades out.
# Used by tools/apply_header_logo.py and tools/build_blog_index.py.
D = 'M14 62 C24 82 66 82 73 56 C77 40 76 24 71 9'
EASE = 'calcMode="spline" keyTimes="0;1" keySplines=".45 0 .25 1"'
FLY = f'begin="0.3s" dur="2.4s" fill="freeze" {EASE}'

def fire(color, width, length, flicker):
    # a short dash whose front end rides exactly under the rocket: offset goes from length to length - 1
    return (f'<path d="{D}" pathLength="1" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round" '
            f'stroke-dasharray="{length} 2" stroke-dashoffset="{length}">'
            f'<animate attributeName="stroke-dashoffset" from="{length}" to="{round(length - 1, 3)}" {FLY}/>'
            f'<animate attributeName="stroke-width" values="{flicker}" dur="0.22s" repeatCount="indefinite"/></path>')

SVG = (
    '<svg class="logo-mark" viewBox="0 0 80 80" width="40" height="40" aria-hidden="true" focusable="false">'
    '<defs><linearGradient id="logo-trail" x1="0" y1="1" x2="1" y2="0"><stop offset="0" stop-color="#15223d" stop-opacity="0"/><stop offset="1" stop-color="#15223d"/></linearGradient>'
    '<filter id="logo-glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="1.4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>'
    '<path d="M40 12 A28 28 0 0 0 40 68 Z" fill="#15223d"/><path d="M40 12 A28 28 0 0 1 40 68 Z" fill="#f5a623"/>'
    '<ellipse cx="40" cy="40" rx="12" ry="28" fill="none" stroke="#fff" stroke-width="3.5"/><path d="M12 40 H68" stroke="#fff" stroke-width="3.5"/>'
    f'<path id="logo-flight" d="{D}" pathLength="1" fill="none" stroke="url(#logo-trail)" stroke-width="2.6" stroke-linecap="round" stroke-dasharray="1 1.1" stroke-dashoffset="1">'
    f'<animate attributeName="stroke-dashoffset" from="1" to="0" {FLY}/></path>'
    # fire: hidden until take-off, fades out after landing
    '<g filter="url(#logo-glow)" opacity="0"><set attributeName="opacity" to="1" begin="0.3s" fill="freeze"/>'
    '<animate attributeName="opacity" from="1" to="0" begin="2.55s" dur="0.6s" fill="freeze"/>'
    + fire('#ff6a1a', 4.2, 0.16, '3.6;5;3.8;4.6;3.6')
    + fire('#f5a623', 2.8, 0.11, '2.4;3.4;2.6;3.2;2.4')
    + fire('#fff1c2', 1.3, 0.05, '1.1;1.7;1.2;1.6;1.1') +
    '</g>'
    # rocket: hidden until take-off, follows the path; its exhaust flickers in flight
    '<g opacity="0"><set attributeName="opacity" to="1" begin="0.3s" fill="freeze"/>'
    '<animateMotion begin="0.3s" dur="2.4s" fill="freeze" rotate="auto" ' + EASE.replace('calcMode', 'calcMode', 1).replace('keyTimes="0;1"', 'keyPoints="0;1" keyTimes="0;1"') + '><mpath href="#logo-flight"/></animateMotion>'
    '<g transform="rotate(90) scale(1.1)">'
    '<path d="M0 6 L-2 11 L0 9.5 L2 11 Z" fill="#f5a623"><animateTransform attributeName="transform" type="scale" values="1 1;1 1.6;1 0.9;1 1.4;1 1" dur="0.2s" begin="0.3s" repeatDur="2.4s" additive="sum"/></path>'
    '<path d="M0 -8 C3.6 -5 3.8 1 2.6 6 H-2.6 C-3.8 1 -3.6 -5 0 -8 Z" fill="#15223d"/>'
    '<path d="M-2.6 2 L-5 7 L-2.4 6 Z M2.6 2 L5 7 L2.4 6 Z" fill="#15223d"/><circle cx="0" cy="-1.5" r="1.4" fill="#fff"/></g></g></svg>'
    # reduced motion: show the finished logo at once
    "<script>/* reduced motion: show the finished logo at once */(function(s){if(window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches&&s&&s.pauseAnimations){s.pauseAnimations();s.setCurrentTime(5);}})(document.currentScript.previousElementSibling);</script>"
)
