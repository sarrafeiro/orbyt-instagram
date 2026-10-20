import numpy as np, wave
SR=44100; BPM=118; beat=60/BPM; bar=4*beat; DUR=60.0
N=int(SR*DUR); L=np.zeros(N); R=np.zeros(N)
rng=np.random.default_rng(7)
def add(sig,t,pan=0.0,g=1.0):
    i=int(t*SR); j=min(N,i+len(sig))
    if i>=N: return
    s=sig[:j-i]*g; L[i:j]+=s*(1-pan)/1; R[i:j]+=s*(1+pan)/1
def env(n,a=0.002,d=0.2):
    t=np.arange(n)/SR; e=np.minimum(1,t/a)*np.exp(-t/d); return e
def lp(x,a):  # one-pole lowpass
    y=np.empty_like(x); s=0.
    for k in range(len(x)): s+=a*(x[k]-s); y[k]=s
    return y
def kick():
    n=int(.35*SR); t=np.arange(n)/SR
    f=50+90*np.exp(-t*30); ph=2*np.pi*np.cumsum(f)/SR
    return np.sin(ph)*np.exp(-t*7)*1.0
def clap():
    n=int(.25*SR); t=np.arange(n)/SR
    x=rng.standard_normal(n); x=x-lp(x,0.08)
    e=np.exp(-t*18)*(1+0.6*np.exp(-((t-0.012)**2)/1e-5))
    return x*e*0.35
def hat(open_=False):
    n=int((.18 if open_ else .05)*SR); t=np.arange(n)/SR
    x=rng.standard_normal(n); x=x-lp(x,0.5)
    return x*np.exp(-t*(15 if open_ else 70))*0.12
def note(f,dur,kind='saw',cut=0.15,a=0.004,d=0.25,g=0.2):
    n=int(dur*SR); t=np.arange(n)/SR
    if kind=='saw':
        x=sum(np.sin(2*np.pi*f*k*t)/k for k in range(1,14) if f*k<12000)
    else: x=np.sin(2*np.pi*f*t)+0.3*np.sin(4*np.pi*f*t)
    x=lp(x,cut)
    return x*env(n,a,d)*g
mid=lambda m:440*2**((m-69)/12)
# Am F C G
prog=[(57,[57,60,64]),(53,[53,57,60]),(48,[48,52,55,60]),(55,[55,59,62])]
arp_cache={}
nbars=int(DUR/bar)+1
for b in range(nbars):
    t0=b*bar
    root,ch=prog[b%4]
    intro=b<1; brk=b in (14,15); out=b>=28
    full=b>=2 and not brk
    # pad
    for m in ch:
        add(note(mid(m+12),bar,'saw',0.03,a=0.05,d=2.5,g=0.08),t0,pan=rng.uniform(-.4,.4))
    for k in range(4):
        tb=t0+k*beat
        if not intro and not brk: add(kick(),tb,g=0.9)
        if full and k in (1,3): add(clap(),tb,g=1)
        if not intro:
            add(hat(),tb+beat/2,pan=0.3)
            if full: add(hat(),tb+beat/4,pan=-0.3,g=0.6); add(hat(),tb+3*beat/4,pan=-0.3,g=0.6)
        # bass offbeat
        if not intro:
            key=('b',root)
            if key not in arp_cache: arp_cache[key]=note(mid(root-12),beat/2*0.9,'saw',0.06,d=0.18,g=0.33)
            add(arp_cache[key],tb+beat/2)
            if full: add(arp_cache[key],tb,g=0.6)
    # pluck arpeggio 16ths
    seq=[ch[0]+12,ch[1]+12,ch[2]+12,ch[1]+12,ch[0]+24,ch[2]+12,ch[1]+12,ch[2]+12]*2
    if True:
        for s,m in enumerate(seq):
            key=('p',m)
            if key not in arp_cache: arp_cache[key]=note(mid(m),0.22,'saw',0.25,d=0.09,g=0.10)
            add(arp_cache[key],t0+s*beat/4,pan=0.35 if s%2 else -0.35, g=(1.0 if full else 0.7))
    # little lead hook on full sections every 2 bars
    if full and b%2==0:
        for s,(m,l) in enumerate([(76,1),(74,1),(72,2),(74,2),(76,2)]):
            pass
        tt=t0
        for m,l in [(ch[0]+24,0.5),(ch[1]+24,0.5),(ch[2]+24,1.0),(ch[1]+24,0.5),(ch[0]+24,1.5)]:
            add(note(mid(m),l*beat,'sine',0.5,a=0.01,d=0.4,g=0.09),tt,pan=0.1); tt+=l*beat
# fade out last 2.5s and in 0.3
t=np.arange(N)/SR
fade=np.clip((DUR-t)/2.5,0,1)*np.clip(t/0.3,0,1)
L*=fade; R*=fade
# simple soft clip + normalize
m=max(abs(L).max(),abs(R).max()); L/=m; R/=m
L=np.tanh(L*1.4)/np.tanh(1.4)*0.85; R=np.tanh(R*1.4)/np.tanh(1.4)*0.85
out=(np.stack([L,R],1)*32767).astype('<i2')
w=wave.open('/tmp/claude-0/sp/v60/musica.wav','wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(out.tobytes()); w.close()
print('ok')
