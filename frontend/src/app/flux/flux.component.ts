import { Component, OnInit } from '@angular/core';
import { WebAPIService } from '../web-api.service';
import { Response } from './flux';

@Component({
  selector: 'app-flux',
  templateUrl: './flux.component.html',
  styleUrls: ['./flux.component.css']
})
export class FluxComponent implements OnInit {
  response: any;
  pages: number [] = [];
  constructor(private apiService: WebAPIService) { }

  ngOnInit(): void {
    this.apiService.getFluxMany().subscribe({
      next: (data) => {
        this.response = data;
        let numbers = [];
        for(let i=0; i < this.response.pages; i++){
          numbers.push(i + 1);
        }
        this.pages = numbers;
      },
      error: (e) => {
        console.log(e);
      }
    })
  }

  paginate(pageNumber: number){
    this.apiService.paginate(pageNumber).subscribe({
      next: (data) => {
        this.response = data;
      },
      error: (e) => {
        console.log(e);
      }
    })
  }

  // paginateNextPrevious(url: string){
  //   this.apiService.paginateNextPrevious(url).subscribe({
  //     next: (data) => {
  //       this.response = data;
  //     },
  //     error: (e) => {
  //       console.log(e);
  //     }
  //   })
  // }
  

}
