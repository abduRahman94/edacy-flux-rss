import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Response } from './flux/flux';

let headers = new HttpHeaders({
  'Content-Type': 'application/json',
});

@Injectable({
  providedIn: 'root'
})
export class WebAPIService {
  api_url = 'http://127.0.0.1:8000/api/flux/';

  constructor(private httpClient: HttpClient) { }

  getFluxMany() {
    return this.httpClient.get< Response [] >(this.api_url, {'headers': headers});
  }

  paginate(pageNumber: number){
    let url = this.api_url + '?page=' + pageNumber;
    return this.httpClient.get< Response [] >(url, {'headers': headers});
  }

  paginateNextPrevious(urlString: string){
      return this.httpClient.get< Response [] >(urlString, {'headers': headers});
  }

}
