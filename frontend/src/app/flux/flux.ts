export interface Flux {
  title: string,
  description: string,
  image: string,
}

export interface Response {
  count: number,
  next: string,
  previous: string,
  results: Flux [],
  pages: number
}