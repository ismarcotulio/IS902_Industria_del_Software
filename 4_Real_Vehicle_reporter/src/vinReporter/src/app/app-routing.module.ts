
import { NgModule } from '@angular/core';
import { RouterModule, Routes} from '@angular/router';

import { LayoutDefaultComponent } from './layout/layout-default/layout-default.component';


const routes: Routes = [
  {
    path: "",
    component: LayoutDefaultComponent,
    children: [
      {
         path: "home",
         loadChildren: () => import('./home/home.module').then(m => m.HomeModule)
      },
      {
        path: "reporter",
        loadChildren: () => import('./reporter/reporter.module').then(m => m.ReporterModule)
     },
      {
        path: "",
        redirectTo: "home",
        pathMatch: "full"
      }
    ]
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
