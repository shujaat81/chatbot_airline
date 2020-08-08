import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomePage } from './home.page';

const routes: Routes = [
  {
    path: 'home',
    component: HomePage,
    children: [
        {
            path: 'fares',
            loadChildren: () => 
            import('../pages/fares/fares.module').then(
                m => m.FaresPageModule
                )
        },
        {
            path: 'market',
            loadChildren: () => 
            import('../pages/market/market.module').then(
                m => m.MarketPageModule
                )
        },
        {
            path: 'chat',
            loadChildren: () => 
            import('../pages/chat/chat.module').then(
                m => m.ChatPageModule
                )
        },
        {
            path: 'info',
            loadChildren: () => 
            import('../pages/info/info.module').then(
                m => m.InfoPageModule
                )
        }
        // {
        //     path: 'settings',
        //     loadChildren: () => 
        //     import('../pages/settings/settings.module').then(
        //         m => m.SettingsPageModule
        //         )
        // }
    ]
}];



@NgModule({
      imports: [RouterModule.forChild(routes)],
      exports: [RouterModule]
    })
export class HomeRouter{}
