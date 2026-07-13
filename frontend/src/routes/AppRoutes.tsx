import { Navigate, Route, Routes } from 'react-router-dom';

import { DashboardPage } from '../features/dashboard/DashboardPage';
import { DashboardLayout } from '../layouts/DashboardLayout';

export function AppRoutes() {
  return (
    <Routes>
      <Route element={<DashboardLayout />}>
        <Route index element={<Navigate to="/dashboard" replace />} />
        <Route path="dashboard" element={<DashboardPage />} />
        <Route path="campaigns" element={<DashboardPage />} />
        <Route path="audiences" element={<DashboardPage />} />
        <Route path="insights" element={<DashboardPage />} />
      </Route>
    </Routes>
  );
}
