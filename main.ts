import { execSync } from "node:child_process";
import { mkdir } from "node:fs/promises";

await mkdir("/output", { recursive: true });
execSync("bash clip.sh /output", { stdio: "inherit" });
console.log("clip.mp4 → /output/clip.mp4");