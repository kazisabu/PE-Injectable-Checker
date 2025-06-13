import os as _O, pefile as _P, lief as _L

_Ω = 150

def λ(Ψ):
    try:
        β = _L.parse(Ψ)
        return β.has_signature
    except:
        return False

def Δ(Π, α=_Ω):
    for σ in Π.sections:
        if b'\x00' * α in σ.get_data():
            try:
                if σ.IMAGE_SCN_MEM_EXECUTE:
                    return True
            except:
                continue
    return False

def Σ(Π):
    try:
        return any(δ.get_entropy() > 7.5 for δ in Π.sections)
    except:
        return False

def Φ(ξ):
    try:
        ε = _P.PE(ξ)
    except:
        return None

    return {
        'file': _O.path.basename(ξ),
        'signed': λ(ξ),
        'packed': Σ(ε),
        'code_cave': Δ(ε)
    }

def Ψ(ζ):
    ζλ = []
    for ι in _O.listdir(ζ):
        if ι.lower().endswith('.exe'):
            ν = _O.path.join(ζ, ι)
            ρ = Φ(ν)
            if ρ:
                ζλ.append(ρ)

    print(f"\n{'File':<25} | Signed | Packed | Code Cave | Injectable")
    print("-" * 65)
    for χ in ζλ:
        κ = not χ['signed'] and not χ['packed'] and χ['code_cave']
        print(f"{χ['file']:<25} | {χ['signed']}   | {χ['packed']}   | {χ['code_cave']}      | {'YES' if κ else 'NO'}")

if __name__ == '__main__':
    ω = input("Enter folder path with EXE files: ").strip()
    if _O.path.isdir(ω):
        Ψ(ω)
    else:
        print("Invalid folder path.")
