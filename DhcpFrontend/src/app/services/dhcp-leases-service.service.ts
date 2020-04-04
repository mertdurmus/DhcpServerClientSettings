import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { throwError, Observable } from 'rxjs';
import { Lease } from '../models/lease';
import { tap, catchError } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class DhcpLeasesServiceService {

  constructor(private http: HttpClient) { }

  path = 'http://127.0.0.1:5000/api';



getLeases(): Observable<Lease[]> {

  return this.http.get<Lease[]>(this.path + '/leases').pipe(
    tap(data => console.log(JSON.stringify(data))),
    catchError(this.handleError)
  );

}

  handleError(err: HttpErrorResponse) {
    let errorMessage = '';
    if (err.error instanceof ErrorEvent) {
   errorMessage = 'bir hata oluştu' + err.error.message;
   } else {
     errorMessage = 'sistemsel bir hata';
   }

    return throwError (errorMessage);
  }

}
