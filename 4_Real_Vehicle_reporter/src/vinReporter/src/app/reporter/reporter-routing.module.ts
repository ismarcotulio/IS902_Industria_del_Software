import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ReporterViewComponent } from './reporter-view/reporter-view.component';

const routes: Routes = [
  {
    path:'',
    component:ReporterViewComponent
  },
  {
    path:':vin',
    component:ReporterViewComponent
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ReporterRoutingModule { }
