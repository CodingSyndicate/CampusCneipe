export const prerender = true;
export const trailingSlash = 'always';
function convert_date(date) {
  let options = {
    year: '2-digit',
    month: '2-digit',
    day: '2-digit',
      timeZone: 'Europe/Berlin'
  };
  return new Intl.DateTimeFormat('de-DE', options).format(date);
}

export async function load() {
  return {
    compileTime: convert_date(new Date().getTime())
  }
}
