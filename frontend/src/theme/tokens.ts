export const designTokens = {
  colors: {
    surface: '#ffffff',
    surfaceMuted: '#f8fafc',
    surfaceElevated: '#ffffff',
    border: '#e2e8f0',
    borderSubtle: 'rgba(148, 163, 184, 0.22)',
    ink: '#0f172a',
    inkMuted: '#64748b',
    brand: '#111827',
    brandAccent: '#4f46e5',
    success: '#16a34a',
    warning: '#d97706',
    danger: '#dc2626',
    info: '#2563eb',
  },
  radii: {
    sm: 10,
    md: 16,
    lg: 24,
    xl: 32,
    pill: 999,
  },
  shadows: {
    card: '0 18px 45px rgba(15, 23, 42, 0.06)',
    elevated: '0 24px 80px rgba(15, 23, 42, 0.12)',
    focus: '0 0 0 4px rgba(79, 70, 229, 0.18)',
  },
  spacing: {
    section: 4,
    card: 3,
  },
} as const;

export type Priority = 'High' | 'Medium' | 'Low';

export const priorityColors: Record<Priority, 'error' | 'warning' | 'success'> = {
  High: 'error',
  Medium: 'warning',
  Low: 'success',
};
