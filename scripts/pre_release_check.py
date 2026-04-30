import os
import subprocess
import sys


def run_command(cmd, desc):
    print(f"\n>>> Running: {desc} ({cmd})")
    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f"✅ {desc} Passed")
    except subprocess.CalledProcessError:
        print(f"❌ {desc} Failed")
        sys.exit(1)


def main():
    # 1. Lint & Type Check
    run_command("pre-commit run --all-files", "Pre-commit Checks")

    # 2. Unit Tests
    run_command("pytest", "Unit Tests")

    # 3. Build Check
    if os.path.exists("dist"):
        import shutil

        shutil.rmtree("dist")

    run_command("pip install build && python -m build", "Package Building")

    # 4. Artifact Verification
    dist_files = os.listdir("dist")
    print(f"\n📦 Generated Artifacts: {dist_files}")
    if not any(f.endswith(".whl") for f in dist_files) or not any(f.endswith(".tar.gz") for f in dist_files):
        print("❌ Missing wheel or sdist!")
        sys.exit(1)

    print("\n" + "=" * 30)
    print("🚀 ALL LOCAL CHECKS PASSED!")
    print("You can now safely push your tag.")
    print("=" * 30)


if __name__ == "__main__":
    main()
