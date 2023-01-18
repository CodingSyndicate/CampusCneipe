import { spawnSync } from 'node:child_process';
export const prerender = true;
export const trailingSlash = 'always';
function convert_date(date) {
  let options = {
    year: '2-digit',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
      timeZone: 'Europe/Berlin'
  };
  return new Intl.DateTimeFormat('de-DE', options).format(date);
}

export async function load() {
  let modTime = spawnSync("git", ['--no-pager', 'log', '-1', '--date=format:%d.%m.%y,%H:%M',  '--format=%ad %h']).stdout.toString();
  return {
    compileTime: convert_date(new Date().getTime()),
    modificationTime: modTime
  }
}
