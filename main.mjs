import { existsSync, mkdirSync } from "node:fs";
import { execSync } from "node:child_process";

const OUT = process.env.OUTPUT_DIR || "/tmp/mkfun-builds/gta6-clipper-01/output";
if (!existsSync(OUT)) mkdirSync(OUT, { recursive: true });

console.log("Clipping GTA 6 trailer...");
execSync("bash clip.sh " + OUT, { stdio: "inherit", env: { ...process.env, OUTPUT_DIR: OUT } });

const clip = OUT + "/clip.mp4";
if (existsSync(clip)) {
  console.log("Clip generated: " + clip);
} else {
  console.error("ERROR: clip.mp4 not found (yt-dlp may have failed, check network)");
  process.exit(1);
}
